import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import query
from core.flight.models import *
from django.http import HttpResponse, JsonResponse
from core.flight.models import *
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from core.flight.forms import *
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.models import User


class flightsView(ListView):
    model = flight
    template_name = "list_flights.html"

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return flight.objects.all()
        else:
            return flight.objects.filter(depart_time__month=4)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Vuelos disponibles"
        return context
    
class flightsReservationsView(ListView):
    model = booking
    template_name = "flight_reservation_list.html"

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    url = 'http://api.openweathermap.org/data/2.5/weather?q=tulua&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
    city = 'Tulua'

    r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'description': r['weather'][0]['description'],
        'icon': r['weather'][0]['icon'],
    }

    def get_queryset(self):
        query = self.model.objects.filter(user_reservation = self.request.user.id)
        return query
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Vuelos reservados"
        context['city_weather'] = self.city_weather
        return context


class DetailFlightView(DetailView):
    model = flight
    template_name = "detail_flight.html"

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detalles del vuelo"
        return context

class flightsCreateView(CreateView):
    model = flight
    form_class = flightsForm
    template_name = "flight_create.html"
    success_url = reverse_lazy("Flights")

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Agregar un vuelo"
        return context


class flightsUpdateView(UpdateView):
    model = flight
    form_class = flightsForm
    template_name = "flight_create.html"
    success_url = reverse_lazy("Flights")

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Editar vuelo"
        return context

class flightsDeleteView(DeleteView):
    model = flight
    template_name = "list_flights.html"
    success_url = reverse_lazy("Flights")

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Detalle vuelo"
        return context


class flightReservation(CreateView):
    model = booking
    success_url = reverse_lazy("Flights")

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @xframe_options_exempt
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            flights = flight.objects.filter(id=request.POST.get("flight")).first()
            if flights:
                new_booking = self.model(
                    flight=flights
                )
                new_booking.save()
                response = JsonResponse({"url": self.success_url})
                response.status_code = 201
                return response
        return redirect("Flights")

class airlineCreateView(CreateView):
    model = airline
    form_class = airlineForm
    template_name = "new_airline.html"
    success_url = reverse_lazy("Flights")

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Agregar una aerolinea"
        return context

class airportCreateView(CreateView):

    model = airport
    form_class = airportForm
    template_name = "new_airport.html"
    success_url = reverse_lazy("Flights")

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Agregar un aeropuerto"
        return context
    
