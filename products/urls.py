from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('', views.BrandViewSet)

urlpatterns = [
    path('', views.ProductListAPIView.as_view()),
    path('create/', views.ProductCreateAPIView.as_view()),
    path('brand/', include(router.urls)),
    path('detail/<int:pk>/', views.ProductDetailDeleteUpdateAPIView.as_view()),

]
