from django.urls import path

from .views import home, about, contact, donate, team, testimonial, service, causes, get404

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('donate', donate, name='donate'),
    path('team', team, name='team'),
    path('service', service, name='service'),
    path('testimonial', testimonial, name='testimonial'),
    path('causes', causes, name='causes'),
    path('get404', get404, name='get404'),
]