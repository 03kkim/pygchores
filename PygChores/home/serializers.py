from rest_framework.serializers import ModelSerializer

from .models import ScheduledEvent

class EventSerializer(ModelSerializer):
    class Meta:
        model = ScheduledEvent
        fields = (
            'id', 'name', 'start_time', 'end_time'
        )