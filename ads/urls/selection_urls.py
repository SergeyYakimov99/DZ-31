from django.urls import path
from ads.views import *

urlpatterns = [
    path('', SelectionListView.as_view()),
    path('<int:pk>/', SelectionDetailView.as_view()),
    path('update/<int:pk>/', SelectionUpdateView.as_view()),
    path('create/', SelectionCreateView.as_view()),
    path('delete/<int:pk>/', SelectionDeleteView.as_view()),
]
