from rest_framework import serializers
from monitoring.models import Website, DowntimeLog
from datetime import datetime


class DowntimeLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DowntimeLog
        fields = ('id',  'downtime_start', 'downtime_end',
                  'downtime_duration', 'error', 'http_status', 'response_time')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     # if not data["downtime_start"]:
    #     downtime_start = data['downtime_start']
    #     # downtime_start = downtime_start.replace(tzinfo=None)
    #     date_format = "%Y-%m-%d %H:%M:%S"
    #     downtime_start = datetime.fromisoformat(downtime_start)
    #     curr_time = datetime.now().replace(tzinfo=None)
    #     downtime_duration = curr_time - downtime_start
    #     data['downtime_duration'] = downtime_duration
    #     return data


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = ['id', 'url', 'created_time', 'auth_scheme']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['auth_scheme'] = instance.auth_scheme.split(',')
        return data


class WebsiteDetailSerializer(serializers.ModelSerializer):
    logs = serializers.SerializerMethodField()

    class Meta:
        model = Website
        fields = ['id', 'url', 'logs']

    def get_logs(self, obj):
        logs = DowntimeLog.objects.filter(website=obj)
        serializer = DowntimeLogSerializer(logs, many=True)
        return serializer.data


