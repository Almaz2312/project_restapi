from django.urls import path
from. import views


urlpatterns = [
    path('', views.BasketListAPIView.as_view()),
    path('detail/<int:pk>/', views.BasketDetailUpdateDelete.as_view()),
    path('add/', views.BasketApiView.as_view()),
]