from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password_confirm = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password_confirm')

    def save(self, **kwargs):
        if self.validated_data.get('password') != self.validated_data.get('password_confirm'):
            raise serializers.ValidationError(
                {
                    'password': 'password does not match'
                }
            )
        else:
            user = User(email=self.validated_data.get(
                'email'), username=self.validated_data.get('username'),)
            user.set_password(self.validated_data.get('password'))
            user.save()
        return user
