from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Count


from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.views import JSONWebTokenAPIView
from rest_framework_jwt.views import JSONWebTokenSerializer
from rest_framework import status
from rest_framework.response import Response

from myapp.models import Snippests, Tag
from myapp.serializers import (
    CreateSnippestSerializer,
    TagSerializer,
    UserSerializer
) 


class LoginView(JSONWebTokenAPIView):
    serializer_class = JSONWebTokenSerializer


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateSnippestsView(ListCreateAPIView):
    serializer_class = CreateSnippestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            raise Exception("Permission denied")

        queryset = Snippests.objects.all()
        # .annotate(count=Count('pk'))
        return queryset

    def perform_create(self, serializer):
        serializer.save()

    def create(self, request, *args, **kwargs):
        tag_name = request.data.get('tag')
        title = request.data.get('title')

        tag = Tag.objects.filter(title=tag_name)
        print
        if not tag.exists():
            tag = Tag.objects.create(title=tag_name)
        else:
            tag = tag.first()

        data = {
            'user': request.user.id,
            'tag': tag.id,
            'title': title
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DetailSnippestsView(RetrieveUpdateDestroyAPIView):
    serializer_class = CreateSnippestSerializer
    permission_classes = [IsAuthenticated]
    queryset = Snippests.objects.all()


class CreateTagView(ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()


class DetailTagView(RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]
    queryset = Tag.objects.all()