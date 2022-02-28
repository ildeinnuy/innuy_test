from rest_framework.views import APIView
from rest_framework.response import Response

from notifications.api.serializers import NotificationSerializer
from .. models import Notification


class NotificationApiView(APIView):
    serializer_class = NotificationSerializer

    def get(self, request):
        notifications = Notification.objects.all().values()
        return Response(
            {'Message': 'List fo notifications',
             'Notifications List': notifications})

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
