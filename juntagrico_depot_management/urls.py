from django.urls import re_path
from juntagrico_depot_management import views

urlpatterns = [
    re_path(r'^dm/depot/change/overview$', views.depot_change_overview),
    re_path(r'^dm/depot/change/(?P<subscription_id>.*?)/', views.activate_future_depot),
]
