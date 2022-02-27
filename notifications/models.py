from django.db import models

from accounts.models import Account
from helpers.models import UpdateMixin


class Notification(UpdateMixin):
    class Meta:
        ordering = ("-id",)

    NOTIFICATIONS_TYPE = (
        ('Welcome', 'Welcome'),
        ('Alert', 'Alert')
    )

    account = models.ForeignKey("accounts.Account", on_delete=models.CASCADE)
    seen = models.BooleanField(default=False, blank=True)
    notification_type = models.CharField(choices=NOTIFICATIONS_TYPE, max_length=10)

    def __str__(self):
        return str(self.notification_type)

    @classmethod
    def generate_mass_notification(cls, accounts=Account.objects.none(), **kwargs):
        to_notify = accounts or Account.objects.all()
        for account in to_notify:
            Notification.objects.create(account=account, **kwargs)
