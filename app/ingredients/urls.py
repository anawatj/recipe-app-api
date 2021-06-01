from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ingredients import views

router = DefaultRouter()
router.register('ingredients', views.IngredientViewSet)

app_name = 'ingredients'

urlpatterns = [
    path('', include(router.urls))
]
