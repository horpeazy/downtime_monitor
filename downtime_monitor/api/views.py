from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from monitoring.models import DowntimeLog, Website
from .models import APIKey
from .serializers import DowntimeLogSerializer, WebsiteSerializer, WebsiteDetailSerializer
import uuid


# Create your views here.
class WebsiteViewSet(viewsets.ModelViewSet):
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    http_method_names = ['get']

class WebsiteDetailView(APIView):
    def get(self, request, pk):
        website = get_object_or_404(Website, pk=pk)
        serializer = WebsiteDetailSerializer(website)
        return Response(serializer.data)

class DowntimeLogViewSet(viewsets.ModelViewSet):
    queryset = DowntimeLog.objects.all()
    serializer_class = DowntimeLogSerializer
    http_method_names = ['get']

class DowntimeLogDetailView(APIView):
    def get(self, request, pk):
        log = get_object_or_404(Website, pk=pk)
        serializer = DowntimeLogSerializer(log)
        return Response(serializer.data)

@csrf_exempt
def generate_apikey(request):
    key = uuid.uuid4()
    api_key = APIKey.objects.create(user=request.user, key=key)
    return JsonResponse({'apikey': key}, status=201)
