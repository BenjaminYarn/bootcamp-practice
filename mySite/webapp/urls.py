from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('cv_page/', views.cv_page, name="cv_page"),
    path('ben/facts/', views.ben_facts, name="ben_facts"),
]