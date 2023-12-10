from rest_framework import serializers

class CreateFirstSerializer(serializers.Serializer):
    title=serializers.CharField()
    
    def validate(self, attrs):
        print(len(attrs.get('title')))
        if attrs.get('title') and len(attrs.get('title'))>20:
            raise serializers.ValidationError('title is too long')
        return attrs
    def to_representation(self,data):
        representation=super().to_representation(data)

        title_value=data.get('title',None)
        if title_value:
            representation['title2']=f"custom {title_value}"
        print(representation)
        return representation
    
