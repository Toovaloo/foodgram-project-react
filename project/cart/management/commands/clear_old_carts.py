from datetime import timedelta

from django.conf import settings
from django.core.management.base import BaseCommand
from django.db.models import F

from cart.models import Cart


class Command(BaseCommand):
    help = 'Deletes old carts of anonymous users'

    def handle(self, *args, **options):
        '''
        Only deletes carts with expired creation_date and owned by
        anonymous users i.e. customer=None.
        '''
        cookie_age = timedelta(seconds=settings.SESSION_COOKIE_AGE)
        old_carts = Cart.objects.filter(
            customer=None,
            creation_date__lt=F('creation_date') + cookie_age
        )
        cnt = old_carts.count()
        old_carts.delete()
        return f'{cnt} old carts deleted.'
