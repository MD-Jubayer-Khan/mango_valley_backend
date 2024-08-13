from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Mango, Order
from .serializers import MangoSerializer, OrderSerializer
from mangoValley.constraints import send_email
from rest_framework.permissions import AllowAny

class MangoViewSet(viewsets.ModelViewSet):
    queryset = Mango.objects.all()
    serializer_class = MangoSerializer
    permission_classes = [AllowAny]

    def list_by_category(self, request):
        category = request.query_params.get('category')
        if category:
            categoryLower = category.lower()
            queryset = self.get_queryset().filter(category__lower=categoryLower)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "Please provide a category parameter"}, status=status.HTTP_400_BAD_REQUEST)

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            order = serializer.save(user=request.user)
            mango = order.mango
            mango.quantity -= 1
            mango.save()
            send_email(request.user, "Order message", "createOrder.html", {"mango":mango}) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        queryset = Order.objects.all()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
    
    @action(detail=True, methods=['post'], url_path='update-status')
    def update_status(self, request, pk=None):
        order = self.get_object()
        new_status = request.data.get('status').upper()
        if new_status not in ['PENDING', 'COMPLETED']:
            return Response({'error': 'Invalid status'}, status=status.HTTP_400_BAD_REQUEST)
        order.status = new_status
        order.save()
        if new_status == 'COMPLETED':
            send_email(order.user, "Order Status message", "orderStatus.html", {"order": order})
        serializer = self.get_serializer(order)
        return Response(serializer.data)
