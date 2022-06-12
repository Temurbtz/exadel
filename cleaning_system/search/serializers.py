from  rest_framework  import serializers


class SearchSerializer(serializers.ModelSerializer):
    text=serializers.CharField()
