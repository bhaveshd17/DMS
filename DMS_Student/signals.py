from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def student_profile(sender, instance, created, **kwargs):
    if created:
        try:
            group = Group.objects.get(name='Student')
            instance.groups.add(group)
            User.objects.create(
                user=instance,
                name=instance.username,
                email=instance.email
            )
        except Group.DoesNotExist:
            # Handle the case where the 'Student' group does not exist
            # This could involve logging the error or creating the group
            pass
