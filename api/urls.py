from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
urlpatterns = [
    path('api/', include(router.urls)),
    path('team/', views.CreateTeam, name='team'),
    path('availability/<int:id>', views.Check_Availability, name='availability'),
    path('tas/', views.tas, name='tas'),
    path('update/<int:id>/', views.UpdateTask, name='update'),

]
