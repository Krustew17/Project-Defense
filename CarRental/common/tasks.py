from datetime import timedelta
from django.contrib.auth import get_user_model
from .models import UserRevenue
from celery import shared_task
from celery import Celery
import logging
from ..rent.models import RentModel
from django.db.models import F
from django.utils import timezone


app = Celery('CarRental')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

logger = logging.getLogger(__name__)

User = get_user_model()


@shared_task
def daily_revenue_reset():
    print("Everyone's revenue has been set to 0")
    today_start = timezone.now().replace(hour=0, minute=0, second=0, microsecond=0)
    UserRevenue.objects.update(revenue_today=0, revenue_last_updated=today_start)


@shared_task
def update_revenue_yesterday():
    start_date = timezone.now() - timedelta(days=2)
    end_date = timezone.now() - timedelta(days=1)
    update_revenue_values(start_date, end_date, 'revenue_yesterday')


def update_revenue_values(start_date, end_date, attribute):
    users = User.objects.all()
    for user in users:
        user_revenue = user.revenue
        rent_models_in_period = RentModel.objects.filter(
            rented_from=user,
            rent_date__gte=start_date,
            rent_date__lte=end_date
        )
        total_revenue = sum(rent_model.calculate_revenue for rent_model in rent_models_in_period)
        setattr(user_revenue, attribute, total_revenue)
        user_revenue.save()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@shared_task
def update_all_revenue_values(user_id):
    update_last_month_revenue.delay(user_id)
    update_last_week_revenue.delay(user_id)
    update_daily_revenue.delay(user_id)


@shared_task
def update_last_week_revenue(user_id):
    start_date = timezone.now() - timedelta(days=7)
    end_date = timezone.now()
    update_user_revenues(start_date, end_date, user_id, 'revenue_last_week')


@shared_task
def update_last_month_revenue(user_id):
    start_date = timezone.now() - timedelta(days=30)
    end_date = timezone.now()
    update_user_revenues(start_date, end_date, user_id, 'revenue_last_month')


@shared_task
def update_daily_revenue(user_id):
    start_date = timezone.now() - timedelta(days=1)
    end_date = timezone.now()
    update_user_revenues(start_date, end_date, user_id, 'revenue_today')


def update_user_revenues(start_date, end_date, user_id, attribute):
    user = User.objects.get(id=user_id)
    user_revenue = user.revenue
    rent_models_in_period = RentModel.objects.filter(
        rented_from=user,
        rent_date__gte=start_date,
        rent_date__lte=end_date
    )
    total_revenue = sum(rent_model.calculate_revenue for rent_model in rent_models_in_period)
    setattr(user_revenue, attribute, total_revenue)
    user_revenue.save()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#
# @shared_task
# def update_car_availability():
#     current_time = timezone.localtime(timezone.now())
#     expired_rentals = RentModel.objects.filter(
#         rent_date__lte=current_time - F('days')
#     )
#
#     for rental in expired_rentals:
#         rental.car_rented.is_available = True
#         rental.car_rented.save()
