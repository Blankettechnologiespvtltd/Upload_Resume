from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import ResumeSerializer

class ResumeUploadAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ResumeSerializer(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            return Response({
                "status": "success",
                "message": "Resume uploaded successfully",
                "data": {
                    "name": instance.full_name,
                    "email": instance.email,
                    "mobile": instance.mobile,
                    "filename": instance.filename,
                    "resume_url": instance.resume.url
                }
            }, status=201)

        return Response(serializer.errors, status=400)