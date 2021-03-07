from core.flight.models import *
from django.urls import reverse_lazy
from core.flight.forms import flightsForm
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView, DeleteView


class flightsView(ListView):
    model = flight
    template_name = 'list_flights.html'

    #def get_queryset(self):
        #return flight.arrival_time.filter()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Vuelos disponibles'
        return  context


class DetailFlightView(DetailView):
    model = flight
    template_name = 'detail_flight.html'
    #context_object_name = 'post'


class flightsCreateView(CreateView):
    model = flight
    form_class = flightsForm
    template_name = 'flight_create.html'
    success_url = reverse_lazy('Flights')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Agregar un vuelo'
        return  context

class flightsUpdateView(UpdateView):
    model = flight
    form_class = flightsForm
    template_name = 'flight_create.html'
    success_url = reverse_lazy('Flights')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar vuelo'
        return  context

class flightsDeleteView(DeleteView):
    model = flight
    template_name = 'list_flights.html'
    success_url = reverse_lazy('Flights')
