from django.urls import path
from . import views

urlpatterns = [
    path('styled/', views.styled_page, name='styled_page'),
]
