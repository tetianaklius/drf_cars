from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

from apps.posts.filters import PostsFilter
from apps.posts.models import PostModel
from apps.posts.serializers import PostCreateListSerializer, PostUpdateSerializer
from core.checkers.profanity_checker import ProfanityChecker
from core.exceptions.profanity_check_exception import ProfanityCheckException
from core.exceptions.property_check_exception import PropertyCheckException
from core.pagination import CustomPagePagination


class PostCreateView(CreateAPIView):  # create post
    serializer_class = PostCreateListSerializer
    queryset = PostModel.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user, is_active=False)

        res = ProfanityChecker.check_profanity(self, data=serializer.validated_data)
        if res:
            serializer.save(profanity_edit_count=0, is_active=True, user_id=user)
        else:
            serializer.save(is_active=False, profanity_edit_count=1, user_id=user)
            raise ProfanityCheckException
        return Response(serializer.data, status.HTTP_201_CREATED)


class PostsListView(ListAPIView):  # all posts
    serializer_class = PostCreateListSerializer
    queryset = PostModel.objects.filter(is_active=True)
    filterset_class = PostsFilter
    pagination_class = CustomPagePagination
    permission_classes = (AllowAny,)


class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):  # post by id
    queryset = PostModel.objects.all()
    serializer_class = PostUpdateSerializer
    http_method_names = ["get", "patch", "delete"]

    def get(self, request, *args, **kwargs):
        permission_classes = (AllowAny,)

    def update(self, request, *args, **kwargs):
        user = self.request.user
        post = self.get_object()
        if user.is_authenticated and self.request.user.id == post.user_id.id:
            serializer = self.get_serializer(data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            # self.perform_update(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PropertyCheckException

    def perform_update(self, serializer):
        post = self.get_object()
        if IsAuthenticated() and self.request.user.id == post.user_id.id:
            serializer.is_valid(raise_exception=True, partial=True)
            serializer.save()
        else:
            raise PropertyCheckException

        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        post = self.get_object()
        if user.IsAuthenticated() and self.request.user.id == post.user_id.id:
            self.destroy(request, *args, **kwargs)
            # post.destroy()
        else:
            raise PropertyCheckException


class PostsListByUserIdView(ListAPIView):  # posts created by some user
    queryset = PostModel.objects.filter(is_active=True)
    serializer_class = PostCreateListSerializer
    permission_classes = (AllowAny,)
    pagination_class = CustomPagePagination
    http_method_names = ["get"]

    def get(self, *args, **kwargs):
        posts = self.queryset.filter(user_id=kwargs["pk"])
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
