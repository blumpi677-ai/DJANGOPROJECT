from rest_framework.viewsets import ModelViewSet
from .models import Job
from .serializers import JobSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

# ✅ Custom Permission
class IsEmployer(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employer'


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all().order_by('-id')
    serializer_class = JobSerializer

    # 🔍 Filters
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['location', 'category']
    search_fields = ['title', 'description']

    # 🔐 Permissions
    def get_permissions(self):
        if self.action == 'create':
            return [IsEmployer()]
        return [IsAuthenticated()]

    # 💼 Assign employer automatically
    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)