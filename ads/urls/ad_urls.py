from django.urls import path
from ads.views import *

urlpatterns = [
    path('', AdListView.as_view(), name='ad_list'),
    path('<int:pk>/', AdDetailView.as_view(), name='ad_detail'),
    path('create/', AdCreateView.as_view(), name='ad_create'),
    path('update/<int:pk>/', AdUpdateView.as_view()),
    path('delete/<int:pk>/', AdDeleteView.as_view()),
    path('<int:pk>/upload_image', AdUploadImageView.as_view()),
]
