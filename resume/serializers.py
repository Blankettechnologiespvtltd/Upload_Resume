from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'

    def validate_email(self, value):
        if Resume.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_mobile(self, value):
        if not value.isdigit() or len(value) < 10:
            raise serializers.ValidationError("Enter valid mobile number")
        return value

    def validate_resume(self, value):
        if not value.name.endswith('.pdf'):
            raise serializers.ValidationError("Only PDF files allowed")

        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("File size should be less than 2MB")

        return value

    def create(self, validated_data):
        file = validated_data.get('resume')

        if file:
            validated_data['filename'] = file.name

        return super().create(validated_data)