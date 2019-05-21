from django.urls import path
from . import views

app_name = "orders"
urlpatterns = [
    path('new/', views.new, name="new"),
    path('show/', views.show, name="show"),
    path('create/', views.create, name="create"),
    path('success/', views.success, name="success"),
    path('<int:id>/create_review/', views.create_review, name="create_review"),
]