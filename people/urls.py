"""contacts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""# will fix this page
from django.urls import path
from .views import PeopleView, PersonView, AddPersonView, UpdatePersonView

urlpatterns = [
    
    path('', PeopleView.as_view(), name='home'), #home page for contacts
    path('contact/<int:pk>', PersonView.as_view(), name='contact'), # where each person's file will be shown
    path('add', AddPersonView.as_view(), name='add-contact'), # where each person will be added
    path('contact/update/<int:pk>', UpdatePersonView.as_view(), name='update-contact'), # where each contact will be updated

]