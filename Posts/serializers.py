from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    titel = serializers.CharField(max_length=100)
    class Meta:
        model=Post
        fields=['id','titel','content','date_posted','author']