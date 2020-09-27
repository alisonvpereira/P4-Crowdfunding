from rest_framework import serializers
from .models import CustomUser
from projects.models import Skill


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    image = serializers.URLField(allow_blank=True)
    website = serializers.URLField(allow_blank=True)
    date_joined = serializers.ReadOnlyField()
    last_login =  serializers.ReadOnlyField()
    skill = serializers.SlugRelatedField('name', many=True,
        queryset=Skill.objects.all())

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        # instance.set_password(validated_data['password'])
        image = validated_data.get('image', instance.image)
        website = validated_data.get('website', instance.website)
        skills = validated_data.pop('skill')
        instance.skill.set = validated_data.get('skill', instance.skill.set(skills))
        instance.save()
        return instance



    