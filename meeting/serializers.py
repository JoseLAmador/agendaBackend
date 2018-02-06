from rest_framework import serializers
from .models import Meeting
from django.contrib.auth.models import User
from accounts.models import Profile


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username', 'id']

class ProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = Profile
		fields = ['id','avatar','username']

class MeetingSerializer(serializers.ModelSerializer):
	user = UserSerializer(many=False, read_only=True)
	participants = ProfileSerializer(many=True, read_only=True)
	class Meta:
		model = Meeting
		fields = '__all__'
