from notifications.api.serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .. models import Notification


class NotificationApiView(APIView):
    serializer_class = NotificationSerializer

    def get(self, request):
        all_notifications = Notification.objects.all().values()
        return Response(
            {'Message': 'List fo notifications',
             'Notifications List': all_notifications})

    def post(self, request):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)
