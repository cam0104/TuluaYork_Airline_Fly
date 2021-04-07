from django.urls import path
from django.views.decorators.http import require_POST
from core.flight import views


urlpatterns = [
     path('flights', views.flightsView.as_view(), name = 'Flights'),
     path('create_flight', views.flightsCreateView.as_view(), name = 'CreateFlight'),
     path('detail_flight/<int:pk>', views.DetailFlightView.as_view(), name = 'DetailFlight'),
     path('update_flight/<int:pk>', views.flightsUpdateView.as_view(), name = 'UpdateFlight'),
     path('delete_flight/<int:pk>', views.flightsDeleteView.as_view(), name = 'DeleteFlight'),
     path('new_reservation', views.flightReservation.as_view(), name = 'newReservation'),
     path('list_reservations', views.flightsReservationsView.as_view(), name = 'listReservations'),
     path('new_airline', views.airlineCreateView.as_view(), name = 'newAirline'),
     path('new_airport', views.airportCreateView.as_view(), name = 'newAirport'),
]