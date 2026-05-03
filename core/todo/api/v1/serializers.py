from rest_framework import serializers
from ...models import TodoModel,Category

class TodoSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source = 'get_snippet')
    relative_url = serializers.URLField(source = 'get_absolute_api_url',read_only = True)
    absolute_url = serializers.SerializerMethodField(method_name='get_abs_url')
    class Meta:
        model = TodoModel
        fields = ['id', 'author','title','text','complete','relative_url','absolute_url','snippet','category']
    
    def get_abs_url(self, obj):
        request = self.context.get("request")
        relative_url = obj.get_absolute_api_url()
        return request.build_absolute_uri(relative_url)
    def to_representation(self, instance):      
        request = self.context.get("request")
        rep = super().to_representation(instance)
        rep['state'] = 'list'
        if request.parser_context.get('kwargs').get('pk'):
            rep['state'] = 'single'
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','level']


