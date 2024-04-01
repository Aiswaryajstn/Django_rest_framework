from django.urls import path
from . import views


urlpatterns = [
   path('', views.searchListView.as_view(), name = 'search')
]