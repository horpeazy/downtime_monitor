from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('downtime-logs', views.DowntimeLogViewSet)
router.register('websites', views.WebsiteViewSet)


app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('websites/<int:pk>', views.WebsiteDetailView.as_view()),
    path('downtime-logs/<int:pk>', views.DowntimeLogDetailView.as_view()),
]
