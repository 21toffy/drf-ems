from rest-framework import serializers

from django.contrib.auth.models import User


class EmployeeSerializer(serializers.HyperLinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'emal',
            'url'
        )
    pass