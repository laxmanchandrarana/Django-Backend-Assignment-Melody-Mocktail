from django.urls import path
from .views import RedirectListCreateView, RedirectDetailView

urlpatterns = [
    path('redirects/', RedirectListCreateView.as_view(), name='redirect-list-create'),
    path('redirects/<int:pk>/', RedirectDetailView.as_view(), name='redirect-detail'),
]
