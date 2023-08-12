from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from rest_framework.mixins import ListModelMixin
from rest_framework.reverse import reverse_lazy
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from .models import Feedback
from .forms import FeedbackForm
from .serializers import FeedbackSerializer


class FeedbackView(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class AddFeedback(CreateView):
    form_class = FeedbackForm
    template_name = 'feedback/add_feedback.html'
    success_url = '/'


class FeedbackViewSet(ListModelMixin, GenericViewSet):
    queryset = Feedback.objects.all().order_by('answered', 'created_at')
    serializer_class = FeedbackSerializer


class UserLoginView(LoginView):
    template_name = 'login-admin.html'
    fields = ('username', 'password')
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main_page')
