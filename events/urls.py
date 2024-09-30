from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/<int:id>', views.event_details, name='details'),
    path('delete/<int:id>', views.event_delete, name='delete'),
    path('edit/<int:id>', views.edit_event, name='edit')
]
