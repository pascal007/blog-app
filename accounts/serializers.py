from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'password']
        extra_kwargs = {'id': {'read_only': True},
                        'password': {'write_only': True}}

    def validate(self, attrs):
        if not attrs['password'] or len(attrs['password']) < 4:
            raise serializers.ValidationError({'password': 'password length must be greater than 4'})
        if not attrs['username'] or len(attrs['username']) < 4:
            raise serializers.ValidationError({'password': 'username length must be greater than 4'})
        if User.objects.filter(username=attrs['username']).exists():
            raise serializers.ValidationError({'username': 'username already exists'})
        attrs['is_active'] = True
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data.get('username'),
            password=validated_data.get('password'),
            is_active=True
        )

