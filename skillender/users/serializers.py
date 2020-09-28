from rest_framework import serializers
from .models import CustomUser, Profile
from projects.models import Skill


class CustomUserSerializer(serializers.Serializer):
    # id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only=True)
    image = serializers.URLField(source='profile.image')



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

        profile_data = validated_data.pop('profile', {})
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        
        for (key, value) in profile_data.items():
            setattr(instance.profile, key, value)
        instance.profile.save()
        return instance


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    # bio = serializers.CharField(allow_blank=True, required=False)
    # image = serializers.URLField()
    # website = serializers.URLField()

    class Meta:
        model = Profile
        # fields = ('username', 'bio', 'image',)
        fields = '__all__'
        read_only_fields = ('username',)



