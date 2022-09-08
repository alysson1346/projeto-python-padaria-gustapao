class SerializerByMethodMixin:
    def get_serializer_class(self, *args, **kwargs):
        return self.serializer_map.get(self.request.method, self.serializer_class)

#Exemplo de mixin:
# class ListCreateProductView(SerializerByMethodMixin, generics.ListCreateAPIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticatedOrReadOnly, IsSeller]

#     queryset = Product.objects.all()
#     serializer_map = {
#         'GET': ProductListSerializer,
#         'POST': ProductDetailSerializer,
#     }

#     def perform_create(self, serializer):
#         serializer.save(seller=self.request.user)
