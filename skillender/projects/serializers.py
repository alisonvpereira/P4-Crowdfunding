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
    date_created = serializers.ReadOnlyField()
    date_updated = serializers.ReadOnlyField()
    owner = serializers.ReadOnlyField(source='owner.username')
    total_pledge_hours = serializers.ReadOnlyField()
    

    def create(self, validated_data):
        categories = validated_data.pop('category')
        project = Project.objects.create(**validated_data)
        project.category.set(categories)
        return project


class PledgeSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    date_created = serializers.ReadOnlyField()
    date_updated = serializers.ReadOnlyField()
    hours = serializers.IntegerField()
    skill = serializers.SlugRelatedField('name', many=True,
        queryset=Skill.objects.all())
    comment = serializers.CharField(max_length=200)
    anonymous = serializers.BooleanField()
    volunteer = serializers.ReadOnlyField()
    project_id = serializers.IntegerField()
    project_title = serializers.ReadOnlyField()


    def create(self, validated_data):
        skills = validated_data.pop('skill')
        pledge = Pledge.objects.create(**validated_data)
        pledge.skill.set(skills)
        return pledge

    def update(self, instance, validated_data):
        instance.hours = validated_data.get('hours', instance.hours)
        skills = validated_data.pop('skill')
        instance.skill.set = validated_data.get('skill', instance.skill.set(skills))
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.volunteer = validated_data.get('volunteer', instance.volunteer)
        instance.project_id = validated_data.get('project_id', instance.project_id)
        instance.save()
        return instance

class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        categories = validated_data.pop('category')
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.category.set = validated_data.get('category', instance.category.set(categories))
        instance.goal_hours = validated_data.get('goal_hours', instance.goal_hours)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


class CategorySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    image = serializers.URLField()

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

class CategoryDetailSerializer(CategorySerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    

class SkillSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=200)
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    image = serializers.URLField()

   
    def create(self, validated_data):
        return Skill.objects.create(**validated_data)

class SkillDetailSerializer(SkillSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


