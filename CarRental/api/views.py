from rest_framework.decorators import api_view
from rest_framework.response import Response
from CarRental.api.serializers import CarModelSerializer
from CarRental.car_app.models import CarModel


# Create your views here.
@api_view(['GET'])
def load_car_models(request):
    make_id = request.GET.get('make_id')
    car_models = CarModel.objects.filter(make_id=make_id)
    serializer = CarModelSerializer(car_models, many=True)
    return Response(serializer.data)
