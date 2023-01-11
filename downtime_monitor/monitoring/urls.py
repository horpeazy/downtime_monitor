from django.urls import path
from .views import website_list, website_detail, create_monitor
from django.views.decorators.csrf import csrf_exempt


app_name = "monitoring"

urlpatterns = [
    path("", website_list, name="website_list"),
    path("create/", csrf_exempt(create_monitor) , name="create_monitor"),
    path('website/<int:website_id>/', website_detail, name='website_detail'),
]