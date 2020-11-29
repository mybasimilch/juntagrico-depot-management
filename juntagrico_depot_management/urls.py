from django.conf.urls import url
from juntagrico_depot_management import views

urlpatterns = [
    url(r'^dm/depot/change/overview$', views.depot_change_overview),
    url(r'^dm/depot/change/(?P<subscription_id>.*?)/', views.activate_future_depot),
]
