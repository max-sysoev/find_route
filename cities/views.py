from django.shortcuts import render, get_object_or_404
from cities.models import City
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from app_libs.dump import dd
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import json
from cities.forms import HtmlForm, CityForm
from django.urls import reverse_lazy

__all__ = (
    'home',
    'CityDetailView',
    'CityCreateView',
    'CityUpdateView',
    'CityDeleteView'
)

def home(request, pk=None):
    # if pk:
    #     city = City.objects.filter(id=pk).first()
    #     city = get_object_or_404(City, id=pk)
    #     context = {'object': city}
    #     return render(request, 'cities/detail.html', context)

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)

    form = CityForm()

    qs = City.objects.all()

    #dump data testing
    # dump_data = dd(request, {'data': "test"})
    # return HttpResponse(dump_data)

    context = {'objects_list': qs, 'form': form}

    #json response testing
    # context = list(City.objects.values())
    # return JsonResponse(context, content_type="application/json", safe=False)

    return render(request, 'cities/home.html', context)

class CityDetailView(DetailView):
    queryset = City.objects.all()
    template_name = 'cities/detail.html'

class CityCreateView(CreateView):
    model = City
    form_class = CityForm
    template_name = 'cities/create.html'

class CityUpdateView(UpdateView):
    model = City
    form_class = CityForm
    template_name = 'cities/update.html'
    success_url = reverse_lazy('cities:home')

class CityDeleteView(DeleteView):
    model = City
    template_name = 'cities/delete.html'
    success_url = reverse_lazy('cities:home')

    # skip confirmation page, bad practice
    # def get(self, request, *args, **kwargs):
    #     return self.delete(request, *args, **kwargs)

