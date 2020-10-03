from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from .models import CustomUser, Profile
from .serializers import CustomUserSerializer, ProfileSerializer
from .permissions import IsCurrentUserOrReadOnly, IsNotAuthenticated


class CustomUserList(APIView):
    permission_classes = [IsNotAuthenticated]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": "success",
                    "response": "User Successfully Created"
                },
                status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomUserDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOrReadOnly
    ]

    def get_slug_field(self):
        return 'user__username'

    def get_object(self, username):
        try:
            user = CustomUser.objects.get(username=username)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, username):
        user = self.get_object(username)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, username):
        user = self.get_object(username)
        data = request.data
        serializer = CustomUserSerializer(instance=user,
                                          data=data,
                                          partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


# class ProfileView(APIView):
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly, IsCurrentUserOrReadOnly
#     ]

#     def get_object(self, username):
#         try:
#             # profile = Profile.objects.select_related('user').get(
#             #     user__username=username
#             # )
#             # self.check_object_permissions(self.request, username)
#             # return username
#             user = CustomUser.objects.get(username=username)
#             self.check_object_permissions(self.request, user)
#             return user
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, username):
#         profile = self.get_object(username)
#         serializer = ProfileSerializer(profile)
#         return Response(serializer.data)

#     def put(self, request, username):
#         profile = self.get_object(username)
#         data = request.data
#         serializer = ProfileSerializer(instance=profile,
#                                        data=data,
#                                        partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(
#             serializer.errors,
#             status=status.HTTP_400_BAD_REQUEST,
#         )


class ProfileView(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsCurrentUserOrReadOnly,
    ]

    def get_object(self, username):
        try:
            user = Profile.objects.select_related('user').get(
                user__username=username)
            self.check_object_permissions(self.request, user)
            return user
            # user = CustomUser.objects.get(username=username)
            # self.check_object_permissions(self.request, user)
            # return user
        except Profile.DoesNotExist:
            raise Http404

    def get(self, request, username):
        profile = self.get_object(username)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def put(self, request, username):
        profile = self.get_object(username)
        data = request.data
        serializer = ProfileSerializer(instance=profile,
                                       data=data,
                                       partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )