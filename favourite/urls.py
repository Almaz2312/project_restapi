from django.urls import path

from . import views


urlpatterns = [
    path('', views.FavouriteListAPIView.as_view()),
    path('add/', views.FavouriteAPIView.as_view()),
    path('delete/<int:pk>/', views.FavouriteDeleteAPIView.as_view()),
]
