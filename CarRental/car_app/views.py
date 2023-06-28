from django.shortcuts import render


# Create your views here.
def create_car_ad(request):
    pass


def edit_car_ad(request, pk):
    pass


def view_car_ad_details(request, pk):
    return render(request, 'car/car_details.html')


def delete_car_ad(request, pk):
    pass
