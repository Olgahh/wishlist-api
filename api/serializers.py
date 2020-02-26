from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Item, FavoriteItem

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name']

    def create(self, validated_data):
        user = User(username=validated_data['username'],first_name = validated_data['first_name'],last_name = validated_data['last_name'] )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','last_name']

class  ItemListSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name = 'api-detail',
        lookup_field = 'id',
        lookup_url_kwarg = 'item_id'
    )
    added_by = UserSerializer()
    favourited = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields =['image', 'name','description','added_by','favourited','detail']

    def get_favourited(self,obj):
        favorites = FavoriteItem.objects.filter(user=obj.added_by)
        count = 0
        for fav in favorites:
            count += 1
        return count


class ItemDetailSerializer(serializers.ModelSerializer):
    favourited_by = serializers.SerializerMethodField()
    class Meta:
        model = Item
        fields =['image', 'name','description','favourited_by']

    def get_favourited_by(self,obj):
        favorites = FavoriteItem.objects.filter(user=obj.added_by)
        return favorites
