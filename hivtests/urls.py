from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_test, name="add"),
    path('results', views.get_daily_results, name='results'),
    path('', include("django.contrib.auth.urls")),

]