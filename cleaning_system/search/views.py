from rest_framework.decorators import api_view
from django.http import Http404, JsonResponse
from  company.serializers  import CompanySerializer
from  company.models  import Company
from django.db.models import Q
@api_view(['GET'])
def search_create(request):
    if request.method == 'GET':
        queryset=Company.objects.filter(
        Q(name__contains=request.data['text'])|
        Q(description__contains=request.data['text'])|
        Q(date_foundation__contains=request.data['text'])|
        Q(operation_area__name__contains=request.data['text'])|
        Q(services__title__contains=request.data['text']) |
        Q(services__description__contains=request.data['text'])|
        Q(services__measurement_unit__contains=request.data['text'])|
        Q(services__per_unit_price__contains=request.data['text'])
        )
        if queryset.exists():
            serializer=CompanySerializer(queryset, many=True)
            return JsonResponse(serializer.data,safe=False)
        return Http404
    return Http404
