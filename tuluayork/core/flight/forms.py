from django import forms
from django.forms import ModelForm, widgets
from tempus_dominus.widgets import DateTimePicker
from core.flight.models import *

class flightsForm(ModelForm):
    class Meta:
        model = flight
        fields = ['airline',
                  'airport_origin',
                  'airport_destination',
                  'destination_name',
                  'depart_time',
                  'arrival_time',
                  'price',
                  'requirements',
                  'n_seat',
                  'status']

        widgets = {
            'n_seat' : widgets.NumberInput(attrs={
                'class': 'form-control',
                'min' : 0
            }),

            'price' : widgets.TextInput(
                attrs={
                    'class' : 'form-control'
                }),

            'status' : widgets.TextInput(attrs={
                'class' : 'form-control'
            }),

            'destination_name': widgets.TextInput(attrs={
                'class': 'form-control'
            })
        }

    depart_time = forms.DateTimeField(widget=DateTimePicker(
        options={
            'useCurrent': True,
            'collapse': False,
        },
        attrs={
            'append': 'fa fa-calendar',
            'icon_toggle': True,
        }))

    arrival_time = forms.DateTimeField(widget=DateTimePicker(
        options={
            'useCurrent': True,
            'collapse': False,
        },
        attrs={
            'class':'datepicker form-control',
            'append': 'fa fa-calendar',
            'icon_toggle': True,
        }))

    requirements = forms.ModelMultipleChoiceField(queryset=requirement.objects.all(),widget=forms.CheckboxSelectMultiple)

class airlineForm(ModelForm):
    class Meta:
        model = airline
        fields = ['name']
        
        widgets = {
            'name' :  widgets.TextInput(attrs={
                'class' : 'form-control'
            }),
        }
        
class airportForm(ModelForm):
    class Meta:
        model = airport
        fields = ['name', 'city']
        
        widgets = {
            'name' :  widgets.TextInput(attrs={
                'class' : 'form-control'
            }),
            
            'city' :  widgets.TextInput(attrs={
                'class' : 'form-control'
            }),
        }
    