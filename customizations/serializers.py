from rest_framework import serializers


class PropertySerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    property = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name

    def get_property(self, obj):
        return obj.property_value
