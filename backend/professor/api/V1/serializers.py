from rest_framework import serializers
from accounts.models import Professor, User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework.validators import UniqueValidator


class ProfessorSerializerForCreate(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(max_length=100, write_only=True)
    class Meta:
        model = Professor
        fields = ('username', 'email','password', 'password_confirmation', 'professor_id')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password_confirmation = attrs.get("password_confirmation")
        password = attrs.get("password")
        print (password_confirmation)
        if password != password_confirmation:
            raise serializers.ValidationError("passwords must be match")
        try:
            validate_password(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})

        return super().validate(attrs)


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
