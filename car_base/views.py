from django.views import generic
from django.urls import reverse

from .models import Car


class IndexView(generic.TemplateView):
    template_name = "car_base/index.html"


class CarListView(generic.ListView):
    template_name = "car_base/car_list.html"
    model = Car
    context_object_name = "cars"


class CarDetailView(generic.DetailView):
    template_name = "car_base/car_detail.html"
    model = Car
    context_object_name = "car"


class CarAddView(generic.CreateView):
    model = Car
    fields = "__all__"
    template_name = "car_base/car_add.html"
    success_url = ""


class CarUpdateView(generic.UpdateView):
    template_name = "car_base/car_update.html"
    model = Car
    fields = "__all__"
    context_object_name = "car"


class CarDeleteView(generic.DeleteView):
    template_name = "car_base/car_delete.html"
    model = Car
    context_object_name = "car"

    def get_success_url(self):
        return reverse("car_list")
