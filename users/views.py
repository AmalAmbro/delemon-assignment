from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, viewsets, mixins
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, exceptions

from .serializers import UserSerializer, RegisterSerializer, FileDataSerializer
from .models import User, FileData
from .functions import find_file_type, read_file

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class FileDataViewset(viewsets.GenericViewSet, mixins.ListModelMixin, 
                      mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                      mixins.UpdateModelMixin):
    queryset = FileData.objects.all().order_by('-uploaded_at')
    serializer_class = FileDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["category", "type", "price",]
    ordering_fields = ["price", "unit_no", "uploaded_at"]
    filterset_fields = ["category", "type", "views", "price", "total_sq_ft", \
                        "rate_per_sq_ft", "unit_no", "uploaded_by", "uploaded_at"]
    
    @action(detail=False, methods=['post'])
    def upload(self, request):
        try:
            uploaded_file = request.FILES.get('file')
            file_name = uploaded_file.name
            acceptable_files = ["excel", "pdf", "image"]
            file_type = find_file_type(file_name)

            if file_type not in acceptable_files:
                raise exceptions.APIException("File not supported, Upload Excel or Image or PDF Files")
            
            data = read_file(uploaded_file, file_type)
            for item in data:
                total_area = float(item.get("TotalArea", 0)) or 0
                asking_price = float(item.get("Asking Price", 0)) or 0
                rate_per_sq_ft = asking_price / total_area if total_area else 0

                FileData.objects.create(
                    category=item.get("Floor", ""),
                    type=item.get("Unit Type", ""),
                    views=item.get("View", ""),
                    price=asking_price,
                    total_sq_ft=total_area,
                    rate_per_sq_ft=rate_per_sq_ft,
                    unit_no=item.get("Unit Code", ""),
                    uploaded_by=request.user
                )
                
            return Response({"message": "File data saved"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e.args, status=status.HTTP_400_BAD_REQUEST)
