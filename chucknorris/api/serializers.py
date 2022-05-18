from rest_framework import serializers
from chucknorris.models import Jokes


class JokesSerializer(serializers.ModelSerializer):
    api_id = serializers.SerializerMethodField()

    class Meta:
        model = Jokes
        fields = (
            'api_id',
            'url',
            'value',
            'icon_url'
        )

    def get_api_id(self, obj):
        return obj['id']