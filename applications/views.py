from rest_framework.viewsets import ModelViewSet
from .models import Application
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated

class IsSeeker(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'seeker'


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsSeeker()]
        return [IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)