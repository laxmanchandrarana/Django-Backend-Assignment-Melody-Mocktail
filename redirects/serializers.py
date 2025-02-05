from rest_framework import serializers
from .models import Redirect

class RedirectSerializer(serializers.ModelSerializer):
    
    def validate_position(self, value):
        """
        Ensure the position is a positive integer.
        """
        if value < 1:
            raise serializers.ValidationError("Position must be a positive integer.")
        return value

    class Meta:
        model = Redirect
        fields = '__all__'  # Include all model fields
