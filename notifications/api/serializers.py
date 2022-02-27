from helpers import serializers
from ..models import Notification


class NotificationSerializer(serializers.BaseSerializer):
    class Meta:
        model = Notification
        fields = (
            "account",
            "seen",
            "notification_type"
        )
