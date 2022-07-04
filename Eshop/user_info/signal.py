
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.user.save()