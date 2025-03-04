from django.urls import path
from .views import index,property_unit_view,lease_agreement_view

urlpatterns = [
    path('property/', index, name='index'),
    path('property_unit/', property_unit_view, name = "property_unit"),
    path('lease_agreement/', lease_agreement_view, name='lease_agreement')
]
