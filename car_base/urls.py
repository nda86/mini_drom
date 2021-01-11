from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    IndexView,
    CarAddView,
    CarListView,
    CarDetailView,
    CarUpdateView,
    CarDeleteView
)

urlpatterns = [
    path("", IndexView.as_view(), name="home_page"),
    path("add", CarAddView.as_view(), name="car_add"),
    path("list/<int:pk>", CarDetailView.as_view(), name="car_detail"),
    path("update/<int:pk>", CarUpdateView.as_view(), name="car_update"),
    path("delete/<int:pk>", CarDeleteView.as_view(), name="car_delete"),
    path("list", CarListView.as_view(), name="car_list"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

