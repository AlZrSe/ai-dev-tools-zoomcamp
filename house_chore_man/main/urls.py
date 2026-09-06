from django.urls import path
from . import views

urlpatterns = [
    path('chores/', views.ChoreListView.as_view(), name='chore_list'),
]