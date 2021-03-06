from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import UserCreateSerializer,ItemListSerializer, ItemDetailSerializer
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from .permissions import IsStaffOrUser
from items.models import Item

# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = UserCreateSerializer

class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer
    permission_classes = [AllowAny,]
    filter_backends = [SearchFilter, OrderingFilter,]
    search_fields = ['name']


class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'item_id'
    permission_classes = [IsStaffOrUser,]
