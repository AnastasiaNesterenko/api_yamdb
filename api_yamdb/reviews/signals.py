from django.dispatch import receiver
from django.db.models.signals import post_delete, post_save
from .models import Review
from django.db.models import Avg


@receiver([post_save, post_delete], sender=Review)
def get_rating(sender, instance, **kwargs):
    instance.titles.rating = instance.titles.reviews.aggregate(
        (Avg('score'))['score__avg']
    )
    instance.titles.save()