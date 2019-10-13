from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from adyogiapi.models import Product
from rest_framework import views, status
from adyogiapi.serializers import ProductSerializer


class AdyogiView(views.APIView):
    serializer_class = ProductSerializer
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()

    def get(self, request, pk):
        """
        fetch and return requested product
        :param request:
        :param pk:
        :return:
        """
        try:
            product = Product.objects.get(id=pk)
            serializer = ProductSerializer(product)
            return Response({'product': serializer.data})
        except Product.DoesNotExist:
            return Response({
                'error': 'Requested product does not exist'
            })

    def post(self, request, *args, **kwargs):
        """
        Will create new product entry with valid data provided
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            product_created = serializer.save()
        serializer = ProductSerializer(product_created)
        return Response({
            "success": 'New product created',
            "status": status.HTTP_201_CREATED,
            "products": serializer.data
        })

    def delete(self, request, *args, **kwargs):
        """
        Will delete the product with requested pk value if exist.
        :param kwargs:
        :return:
        """
        pk = kwargs.get('pk')
        try:
            product = Product.objects.get(id=pk)
            product.delete()
            return Response({
                'message': "Product deleted succesfully with id: %s" % pk
            })
        except Product.DoesNotExist:
            return Response({
                'error': 'Product does not exist'
            })
