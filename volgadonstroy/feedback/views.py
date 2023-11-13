from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common_services.mail_service import send_feedback_mail
from .models import Feedback
from .serializers import FeedbackSerializer


class FeedbackCreateView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save()
        obj = serializer.data
        send_result = send_feedback_mail(obj)
        if send_result:
            print("Success", send_result)
        else:
            print("Bad sending")


class FeedbackViewSet(ModelViewSet):
    """Soft delete!!!"""
    http_method_names = ['get', 'patch', 'delete']
    queryset = Feedback.objects.all().order_by('answered', 'created_at')
    serializer_class = FeedbackSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance.answered:
            return Response('Message must be marked as "was answered" for delete.',
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
