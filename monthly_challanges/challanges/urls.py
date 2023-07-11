from django.urls import path
from . import views

urlpatterns = [
  # path("jan", views.showJan),
  # path("feb", views.showFeb),
  # path('some', views.some),
  path("", views.index, name="index"),
  path("<int:month>", views.monthly_challanges_by_number),
  path("<str:month>", views.monthly_challange, name="month-challange")
]
