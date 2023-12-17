from django.urls import path
from catalog.views import main, contacts

urlpatterns = [
    path('', main),
    path('contacts/', contacts)
]