from django.contrib.auth.decorators import login_required
import django.contrib.auth.mixins as mixins
from django.shortcuts import render, redirect
import django.views.generic as views
from django.urls import reverse_lazy
from .models import PhotoCarModel, CarListing
from .forms import AttachPhotosToCar, CreateCarForm, EditCarForm
from ..core.utils import check_user_is_manager


@login_required
def create_ad_view(request):
    if request.method == 'GET':
        form1 = AttachPhotosToCar()
        form2 = CreateCarForm()
    else:
        form1 = AttachPhotosToCar(request.POST, request.FILES)
        form2 = CreateCarForm(request.POST)

        if form1.is_valid() and form2.is_valid():
            car_obj = form2.save(commit=False)
            car_obj.attached_user = request.user
            car_obj.save()
            files = form1.cleaned_data["image"]
            for f in files:
                PhotoCarModel.objects.create(car=car_obj, image=f)

            return redirect('car listings')
    context = {
        'form1': form1,
        'form2': form2,
    }
    return render(request, 'car/create_car.html', context)


class CarListingDetails(views.DetailView):
    template_name = 'car/car_details.html'
    model = CarListing
    context_object_name = 'car_listing'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['car_photos'] = PhotoCarModel.objects.filter(car_id=CarListing.objects.filter(pk=self.object.id).get())
        context['is_manager'] = check_user_is_manager(self.request.user)
        return context


@login_required
def edit_car_listing(request, pk):
    car = CarListing.objects.filter(pk=pk).get()
    car_photos = PhotoCarModel.objects.filter(car=car).first()

    if request.method == 'GET':
        form1 = EditCarForm(instance=car)
    else:
        form1 = EditCarForm(request.POST, instance=car)
        print(car_photos)
        if form1.is_valid():
            form1.save()
            return redirect(reverse_lazy('car ad details', kwargs={'pk': pk}))

    context = {
        'car_form': form1,
        'pk': pk
    }

    return render(request, 'car/edit_car_listing.html', context)


class DeleteCarView(mixins.LoginRequiredMixin, views.DeleteView):
    template_name = 'car/delete_car.html'
    context_object_name = 'car_listing'
    model = CarListing

    def get_success_url(self):
        return reverse_lazy('car listings')
