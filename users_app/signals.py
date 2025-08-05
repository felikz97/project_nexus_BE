# users_app/signals.py
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
import logging

User = get_user_model()

@receiver(post_save, sender=User)
def assign_default_group(sender, instance, created, **kwargs):
    if created:
        # For example: default new users = "Customer"
        group, _ = Group.objects.get_or_create(name='Customer')
        instance.groups.add(group)

@receiver(user_logged_in)
def log_login(sender, request, user, **kwargs):
    print(f"{user.username} logged in at {request.META.get('REMOTE_ADDR')}")