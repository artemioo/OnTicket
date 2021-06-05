from django.db.models.signals import post_save
from django.dispatch import receiver

from main.models import Matches, Tickets


@receiver(post_save, Matches)
def generation(sender, instance, created=True, **kwargs):
    if created:
        return None

    ticket_list = Tickets.objects.bulk_create([
        Tickets(match=instance, number=f'{instance.slug}-{ticket + 1}')
        for ticket in range(instance.total_tickets)
    ])
