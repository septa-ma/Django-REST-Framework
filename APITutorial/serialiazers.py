from rest_framework import serializers
from .models import Post

# createing a serializer for a model
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'title', 
            'description',
            'owner'
        )

 
# createing a form for a model
# working with serializer is the same as form
# from django import forms

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = (
#             'title', 
#             'description'
#         )