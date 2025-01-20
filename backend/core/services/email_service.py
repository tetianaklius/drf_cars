import os

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model

from core.services.jwt_service import JWTService, ActivateToken
from configs.celery import app

UserModel = get_user_model()


class EmailService:
    @staticmethod
    @app.task
    def __send_email(to: str, template_name: str, context: dict, subject: str) -> None:
        template = get_template(template_name)
        html_content = template.render(context)
        msg = EmailMultiAlternatives(
            to=[to],
            from_email=os.environ.get("EMAIL_HOST_USER"),
            subject=subject
        )
        msg.attach_alternative(html_content, mimetype="text/html")
        msg.send()

    @classmethod
    def registration(cls, user):
        token = JWTService.create_token(user, ActivateToken)
        url = f"http://localhost/activate/{token}"
        cls.__send_email.delay(
            to=user.email,
            template_name="registration.html",
            context={"name": user.profile.name, "url": url},
            subject="Registration confirm"
        )

    @staticmethod
    @app.task
    def spam():
        for user in UserModel.objects.all():
            EmailService.__send_email(user.email, "spam.html", {}, "spam")

