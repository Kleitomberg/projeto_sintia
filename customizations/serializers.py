from rest_framework import serializers
from customizations.models import screenSides,fontFamilies



class SidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = screenSides
        fields = ("name", "id", "prop", "value","property_value")
        read_only_fields = ("id",)
        

class FontSerializer(serializers.ModelSerializer):
    class Meta:
        model = fontFamilies
        fields = ("name", "id", "prop", "value","property_value")
        read_only_fields = ("id",)

class PropertySerializer(serializers.Serializer):
    
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    property = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj.id
    
    def get_name(self, obj):
        return obj.name

    def get_property(self, obj):
        return obj.property_value
    
