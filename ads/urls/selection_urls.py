from django.urls import path
from ads.views import *

urlpatterns = [
    path('', SelectionListView.as_view(), name='selection_list'),
    path('<int:pk>/', SelectionDetailView.as_view()),
    path('update/<int:pk>/', SelectionUpdateView.as_view()),
    path('create/', SelectionCreateView.as_view(), name='selection_create'),
    path('delete/<int:pk>/', SelectionDeleteView.as_view()),
]
