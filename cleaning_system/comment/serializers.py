from  rest_framework  import serializers
from  .models  import Comment

class CommentSerializer(serializers.ModelSerializer):
    username=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=["text","username"]

    def  get_username(self,obj):
        return obj.user.username
