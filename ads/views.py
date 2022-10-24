from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, UpdateView, DeleteView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Category, Ad, Selection
from ads.permissions import IsOwnerSelection, IsOwnerAdOrStaff
from ads.serializers import AdListSerializer, SelectionCreateSerializer, SelectionListSerializer, \
    SelectionDetailSerializer, AdUpdateSerializer, CategorySerializer, AdDetailSerializer, AdCreateSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def root(request):
    return JsonResponse({'status': 'ok'})


"""
добавили методы CRUD для категорий и объявлений
"""


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({'id': cat.id, 'name': cat.name}, safe=False,
                            json_dumps_params={'ensure_ascii': False})


class AdListView(ListAPIView):
    """
    Поиск объявлений по разным фильтрам + сортировка
    """

    queryset = Ad.objects.order_by("-price").all()
    serializer_class = AdListSerializer

    # def get(self, request, *args, **kwargs):
    #     categories = request.GET.getlist('cat', [])
    #     if categories:
    #         self.queryset = self.queryset.filter(category_id__in=categories)
    #     text = request.GET.get('text')
    #     if text:
    #         self.queryset = self.queryset.filter(name__icontains=text)
    #     location = request.GET.get('location')
    #     if location:
    #         self.queryset = self.queryset.filter(author__location__name__icontains=location)
    #     price_from = request.GET.get('price_from')
    #     price_to = request.GET.get('price_to')
    #     if price_from:
    #         self.queryset = self.queryset.filter(price__gte=price_from)
    #     if price_to:
    #         self.queryset = self.queryset.filter(price__lte=price_to)
    #
    #     return super().get(self, *args, **kwargs)


# @method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateAPIView):
    model = Ad
    serializer_class = AdCreateSerializer

    # fields = ['name', 'author_id', 'category', 'price', 'description', 'is_published']
    #
    # def post(self, request, *args, **kwargs):
    #     data = json.loads(request.body)
    #     author = get_object_or_404(User, id=data['author_id'])
    #     category = get_object_or_404(User, id=data['category_id'])
    #     new_ad = Ad.objects.create(
    #         name=data['name'],
    #         author=author,
    #         category=category,
    #         price=data['price'],
    #         description=data['description'],
    #         is_published=data['is_published'] if 'is_published' in data else False
    #     )
    #
    #     return JsonResponse({"id": new_ad.id,
    #                          "name": new_ad.name,
    #                          "author": new_ad.author.username,
    #                          "price": new_ad.price,
    #                          "description": new_ad.description,
    #                          "is_published": new_ad.is_published}, safe=False,
    #                         json_dumps_params={'ensure_ascii': False})


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerAdOrStaff]


class AdDeleteView(DeleteView):
    queryset = Ad.objects.all()
    serializer_class = AdUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerAdOrStaff]


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get("image")
        self.object.save()
        return JsonResponse({'id': self.object.id,
                             'name': self.object.name,
                             'author': self.object.author.username,
                             'price': self.object.price,
                             'description': self.object.description,
                             'category': self.object.category.name,
                             'is_published': self.object.is_published,
                             'image': self.object.image.url},
                            safe=False, json_dumps_params={'ensure_ascii': False})


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdDetailSerializer
    permission_classes = [IsAuthenticated]


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated, IsOwnerSelection]


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateSerializer
    permission_classes = [IsAuthenticated]
