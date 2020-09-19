from rest_framework import serializers
from .models import Project, Pledge, Category, Skill

class ProjectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    category = serializers.SlugRelatedField('name', many=True,
        queryset=Category.objects.all())
    goal_hours = serializers.IntegerField()
    image = serializers.URLField()
    is_open = serializers.BooleanField()
    date_created = serializers.DateTimeField()
    owner = serializers.ReadOnlyField(source='owner.id')
    

    def create(self, validated_data):
        categories = validated_data.pop('category')
        project = Project.objects.create(**validated_data)
        project.category.set(categories)
        return project


class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    hours = serializers.IntegerField()
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    volunteer = serializers.CharField(max_length=200)
    project_id = serializers.IntegerField()

    def create(self, validated_data):
        return Pledge.objects.create(**validated_data)

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
        instance.description)
        instance.goal_hours = validated_data.get('goal_hours', instance.goal_hours)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open',
        instance.is_open)
        instance.date_created = validated_data.get('date_created',
        instance.date_created)
        instance.owner = validated_data.get('ownder',
        instance.owner)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class CategoryDetailSerializer(CategorySerializer):

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    

class SkillSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)

    def create(self, validated_data):
        return Skill.objects.create(**validated_data)


