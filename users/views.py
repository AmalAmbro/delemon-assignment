from rest_framework import generics, permissions
from .models import User, FileData
from .serializers import UserSerializer, RegisterSerializer, FileDataSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class FileDataListView(generics.ListAPIView):
    queryset = FileData.objects.all().order_by('-uploaded_at')
    serializer_class = FileDataSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["category", "type", "price",]
    ordering_fields = ["price", "unit_no", "uploaded_at"]
    filterset_fields = ["category", "type", "views", "price", "total_sq_ft", \
                        "rate_per_sq_ft", "unit_no", "uploaded_by", "uploaded_at"]
