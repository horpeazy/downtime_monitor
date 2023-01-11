from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from monitoring.models import DowntimeLog, Website
from .serializers import DowntimeLogSerializer, WebsiteSerializer, WebsiteDetailSerializer


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
