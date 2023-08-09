from rest_framework import serializers
from accounts.models import Professor


class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }