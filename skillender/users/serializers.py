from rest_framework import serializers
from .models import CustomUser, Profile
from projects.models import Skill
from projects.serializers import ProjectSerializer, PledgeSerializer


class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    image = serializers.URLField(source='profile.image', required=False)
    is_superuser = serializers.BooleanField(default=0)
    is_staff = serializers.BooleanField(default=0)
    owner_projects = ProjectSerializer(many=True, read_only=True)
    pledges = PledgeSerializer(many=True, read_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create(username=validated_data['username'],
                                         email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        # instance.set_password(validated_data['password'])

        profile_data = validated_data.pop('profile', {})
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)
        instance.profile.save()
        return instance


# class ProfileSerializer(serializers.ModelSerializer):
#     fullname = serializers.CharField(source='profile.fullname')
#     bio = serializers.CharField(source='profile.bio')
#     image = serializers.URLField(source='profile.image')
#     website = serializers.URLField(source='profile.website')
#     created_at = serializers.DateTimeField(source='profile.created_at')
#     updated_at = serializers.DateTimeField(source='profile.updated_at')
#     skills = serializers.SlugRelatedField('name',
#                                           many=True,
#                                           queryset=Skill.objects.all())
#     owner_projects = ProjectSerializer(many=True, read_only=True)
#     pledges = PledgeSerializer(many=True, read_only=True)

#     class Meta:
#         model = CustomUser
#         fields = ('id', 'username', 'email', 'fullname', 'website', 'image',
#                   'date_joined', 'created_at', 'updated_at', 'last_login',
#                   'bio', 'skills', 'owner_projects', 'pledges')
#         # fields = '__all__'
#         # read_only_fields = ('username', 'pledges')

#     def update(self, instance, validated_data):
#         skills = validated_data.pop('skills')
#         instance.skills.set = validated_data.get('skills',
#                                                  instance.skills.set(skills))

#         profile_data = validated_data.pop('profile', {})
#         for (key, value) in validated_data.items():
#             setattr(instance, key, value)
#         instance.save()

#         for (key, value) in profile_data.items():
#             setattr(instance.profile, key, value)
#         instance.profile.save()
#         return instance


class ProfileSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(max_length=50)
    bio = serializers.CharField()
    image = serializers.URLField()
    website = serializers.URLField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    username = serializers.ReadOnlyField(source='user.username')
    user = CustomUserSerializer()

    skills = serializers.SlugRelatedField('name',
                                          many=True,
                                          queryset=Skill.objects.all())

    class Meta:
        model = Profile
        fields = (
            'id',
            'username',
            'user',
            'fullname',
            'website',
            'image',
            'created_at',
            'updated_at',
            'bio',
            'skills',
        )