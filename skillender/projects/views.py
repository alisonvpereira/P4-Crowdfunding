from django.http import Http404
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, Category, Skill
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, CategorySerializer, CategoryDetailSerializer, SkillSerializer, SkillDetailSerializer
from .permissions import IsOwnerOrReadOnly, IsStaffOrReadOnly


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(instance=project,
                                             data=data,
                                             partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        project = self.get_object(pk)
        project.delete()
        return Response("Project Deleted", status=status.HTTP_204_NO_CONTENT)


class PledgeList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class PledgeDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        data = request.data
        serializer = PledgeSerializer(instance=pledge, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response("Pledge Deleted", status=status.HTTP_204_NO_CONTENT)


class CategoryList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsStaffOrReadOnly
    ]

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class CategoryDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsStaffOrReadOnly
    ]

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)
        serializer = CategoryDetailSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        data = request.data
        serializer = CategoryDetailSerializer(instance=category,
                                              data=data,
                                              partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response("Category Deleted", status=status.HTTP_204_NO_CONTENT)


class SkillList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsStaffOrReadOnly
    ]

    def get(self, request):
        skill = Skill.objects.all()
        serializer = SkillSerializer(skill, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SkillSerializer(data=request.data)
        if request.user.is_staff:
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED,
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
        return Response(serializer.errors, status=status.HTTP_403)


class SkillDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsStaffOrReadOnly
    ]

    def get_object(self, name):
        try:
            return Skill.objects.get(name=name)
        except Skill.DoesNotExist:
            raise Http404

    def get(self, request, name):
        skill = self.get_object(name)
        serializer = SkillDetailSerializer(skill)
        return Response(serializer.data)

    def put(self, request, name):
        skill = self.get_object(name)
        data = request.data
        serializer = SkillDetailSerializer(instance=skill,
                                           data=data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

    def delete(self, request, name, format=None):
        skill = self.get_object(name)
        skill.delete()
        return Response("Skill Deleted", status=status.HTTP_204_NO_CONTENT)
