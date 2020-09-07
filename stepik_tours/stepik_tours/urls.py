from django.urls import path

from tours.views import DepartureView, MainView, TourView


urlpatterns = [
    path('', MainView),
    path('tour/<int:id>', TourView),
    path('departure/<str:departure>/', DepartureView),
]
