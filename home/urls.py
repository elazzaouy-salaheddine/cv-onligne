from django.urls import path
from .views import Home,portoflio_detail_view


urlpatterns = [
    path('', Home, name='home'),
    path('portfolio/<int:id>', portoflio_detail_view, name='portfolio-detail'),
]