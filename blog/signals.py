from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import BlogPost

@receiver(post_save, sender=BlogPost)
def check_views_count(sender, instance, **kwargs):
    if instance.views_count == 100:
        send_mail(
            'Поздравление!',
            f'Статья "{instance.title}" достигла 100 просмотров!',
            'alena.sarycheva.99@bk.ru',
            ['alena.sarycheva.99@bk.ru'],
            fail_silently=False,
        )