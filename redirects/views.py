from rest_framework import generics, filters
from .models import Redirect
from .serializers import RedirectSerializer

class RedirectListCreateView(generics.ListCreateAPIView):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['position']

    def get_queryset(self):
        queryset = super().get_queryset()
        is_active = self.request.query_params.get('is_active')
        availability = self.request.query_params.get('availability')

        if is_active is not None:
            is_active_bool = is_active.lower() in ['true', '1']
            queryset = queryset.filter(is_active=is_active_bool)
        if availability:
            queryset = queryset.filter(availability=availability)
        return queryset

class RedirectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Redirect.objects.all()
    serializer_class = RedirectSerializer
