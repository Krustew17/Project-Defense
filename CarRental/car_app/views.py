from django.shortcuts import render, redirect
import django.views.generic as views
from django.urls import reverse_lazy
from .filters import CarFilter
from .models import CarModel, PhotoCarModel, CarListing
from .forms import AttachPhotosToCar, CreateCarForm, EditCarForm


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
            # form1.save(commit=False)
            # form2.save()

            return redirect('home page')
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
        return context


def edit_car_listing(request, pk):
    car = CarListing.objects.filter(pk=pk).get()
    car_photos = PhotoCarModel.objects.filter(car=car).first()

    if request.method == 'GET':
        form1 = EditCarForm(instance=car)
        # form2 = AttachPhotosToCar(instance=car_photos)
    else:
        form1 = EditCarForm(request.POST, instance=car)
        # form2 = AttachPhotosToCar(request.POST, instance=car_photos)
        print(car_photos)
        if form1.is_valid():
            form1.save()
            # form2.save()
            return redirect(reverse_lazy('car ad details', kwargs={'pk': pk}))

    context = {
        'car_form': form1,
        # 'photos_form': form2,
        'pk': pk
    }

    return render(request, 'car/edit_car_listing.html', context)


def delete_car_ad(request, pk):
    return render(request, 'car/delete_car.html')


# ~~~~~~~~~ T   E   S   T      A   R   E   A ~~~~~~~~~


def test_html_css(request):
    return render(request, 'car/listing.html')


def test_image(request, pk):
    images = PhotoCarModel.objects.filter(car=CarListing.objects.filter(pk=pk).get())
    # print(images)
    return render(request, 'car/test_again.html', {'images': images})


class TestImage(views.ListView):
    template_name = 'car/test_again.html'
    model = CarModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = PhotoCarModel.objects.filter(car_id=CarModel.objects.filter(pk=58).get())
        return context


class Something(views.ListView):
    template_name = 'car/test1.html'
    model = CarFilter
    queryset = CarListing.objects.all()
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CarFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form
        return context

# ~~~~~~~~~~~ MIGHT NEED LATER ~~~~~~~~~~~
# class TestUploadMultipleImages(FormView):
#     form_class = AttachPhotosToCar
#     template_name = 'car/create_ad.html'  # Replace with your template.
#
#     def get_success_url(self):
#         return reverse_lazy('home page')
#
#     def post(self, request, *args, **kwargs):
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)
#
#     def form_valid(self, form):
#         car_obj = CarModel.objects.filter(pk=1).get()
#         print(form.cleaned_data)
#         files = form.cleaned_data["image"]
#         for f in files:
#             PhotoCarModel.objects.create(car=car_obj, image=f)
#         return super().form_valid(form)


# class TestView(views.CreateView):
#     template_name = 'car/create_car.html'
#     form_class = CreateCarForm
#
#     def get_success_url(self):
#         return reverse_lazy('home page')
#
#     def form_valid(self, form):
#         car_obj = form.save(commit=False)
#         car_obj.attached_user = self.request.user
#         car_obj.save()
#         return super().form_valid(form)
