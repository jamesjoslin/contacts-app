from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Person
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PersonForm
# Where the rubber meets the road between the model and html templates


#main page, where contacts will be listed
class PeopleView(ListView):
    model = Person
    template_name = 'index.html'

# for each contact's individual view
class PersonView(DetailView):
    model = Person
    template_name = 'person.html'

# add a new contact
class AddPersonView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'new.html'


# update a contact
class UpdatePersonView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'edit.html'
