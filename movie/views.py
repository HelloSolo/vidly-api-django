from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .filter import MovieFilter
from .models import Customer, Movie, Genre, MoviePoster, SubcriptionType, WatchList
from .paginate import DefaultPagination
from .permissions import Is_AdminUserOrReadOnly
from .serializers import (
    AddCustomerSerializer,
    AddMovieSerializer,
    CustomerSerializer,
    MoviePosterSerializer,
    MovieSerializer,
    GenreSerializer,
    SubscriptionTypeSerializer,
    WatchListSerializer,
    AddWatchListSerializer,
)


class MovieViewSet(ModelViewSet):
    queryset = Movie.objects.prefetch_related("images").select_related("genre").all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MovieFilter
    pagination_class = DefaultPagination
    permission_classes = [Is_AdminUserOrReadOnly]
    ordering_fields = ["imbdRating", "releaseDate"]
    search_fields = ["title"]

    def get_serializer_class(self):
        if self.request.method == "POST" or self.request.method == "PUT":
            return AddMovieSerializer
        return MovieSerializer

    def paginate_queryset(self, queryset):
        if self.request.headers["Host"] == "localhost:8000":
            return None
        return super().paginate_queryset(queryset)


class MoviePosterViewSet(ModelViewSet):
    serializer_class = MoviePosterSerializer

    def get_queryset(self):
        return MoviePoster.objects.filter(movie_id=self.kwargs["movie_pk"])

    def get_serializer_context(self):
        return {"movie_id": self.kwargs["movie_pk"]}


class GenreViewSet(ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class SubscriptionTypeViewSet(ReadOnlyModelViewSet):
    queryset = SubcriptionType.objects.all()
    serializer_class = SubscriptionTypeSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return CustomerSerializer
        return AddCustomerSerializer

    @action(detail=False, methods=["GET", "PUT"], permission_classes=[IsAuthenticated])
    def me(self, request):
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == "GET":
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == "PUT":
            serializer = AddCustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class WatchListViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WatchList.objects.select_related("movie").filter(
            user_id=self.request.user.id
        )

    def get_serializer_class(self):
        if self.request.method == "GET":
            return WatchListSerializer
        return AddWatchListSerializer

    def get_serializer_context(self):
        return {"user_id": self.request.user.id}
