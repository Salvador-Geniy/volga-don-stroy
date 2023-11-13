from dataclasses import dataclass
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

@dataclass
class FeedbackData:
    id: int
    first_name: str
    last_name: str
    phone: str
    answered: bool
    created_at: str


def send_feedback_mail(feedback_data: dict[str, str]):
    feedback = FeedbackData(**feedback_data)

    html_message = render_to_string('feedback/feedback_message.html', {'feedback': feedback})
    plain_message = strip_tags(html_message)

    # message_to_send = f"Found new message from feedback service:" \
    #                   f"{feedback.first_name} {feedback.last_name}, {feedback.phone}"
    result = send_mail(
                subject="Feedback",
                message=plain_message,
                from_email="feedback@djangosite.tw1.ru",
                recipient_list=["alexderendyaev@yandex.ru"],
                fail_silently=False,
                html_message=html_message,
            )
    return result
