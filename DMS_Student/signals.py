from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save


def student_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='Student')
        instance.groups.add(group)
        User.objects.create(
            user=instance,
            name=instance.username,
            email=instance.email
        )
post_save.connect(student_profile, sender=User)