
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from .views import manage_items, manage_item

#router = routers.DefaultRouter()
#router.register(r"items", manage_items)
#router.register(r"items/<slug:key>", manage_item)

urlpatterns = {
        path("items", manage_items, name="items"),
        path("items/<slug:key>", manage_item, name="single_item")
        }
urlpatterns = format_suffix_patterns(urlpatterns)

