from rest_framework import serializers
from .models import Redirect

class RedirectSerializer(serializers.ModelSerializer):
    # Make image fields optional for updates
    image_phone = serializers.ImageField(required=False)
    image_web = serializers.ImageField(required=False)
    
    class Meta:
        model = Redirect
        fields = '__all__'

    def validate_position(self, value):
        """Ensure position is greater than zero."""
        if value <= 0:
            raise serializers.ValidationError("Position must be a positive integer.")
        return value

    def validate_redirect_url_web(self, value):
        """Ensure the web URL is valid."""
        if not value.startswith("http"):
            raise serializers.ValidationError("Web redirect URL must be a valid HTTP/HTTPS link.")
        return value

    def validate_redirect_url_phone(self, value):
        """Ensure the phone URL is valid."""
        if not value.startswith("http"):
            raise serializers.ValidationError("Phone redirect URL must be a valid HTTP/HTTPS link.")
        return value