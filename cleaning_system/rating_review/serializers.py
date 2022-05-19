from rest_framework import serializers
from  .models  import  Review
from  cleaning_company.models  import Company
from django.contrib.auth.models import User
from  cleaning_company.models  import  Company



class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    review = serializers.CharField()
    rating= serializers.CharField(max_length=20)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all(),many=False)
    


    def create(self, validated_data):
        review=Review()
        review.review=validated_data.get('review')
        review.rating=validated_data.get('rating')
        company=Company.objects.get(pk=validated_data.get("company").id)
        review.company=company
        review.save()
        return review

    def update(self, instance, validated_data):
        instance.review = validated_data.get('review', instance.review)
        instance.rating = validated_data.get('rating', instance.rating)
        instance.company =Company.objects.get(pk=validated_data.get('company', instance.company.id).id)
        return instance


  

