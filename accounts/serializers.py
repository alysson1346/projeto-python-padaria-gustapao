from rest_framework import serializers
from .models import Account

#create, update, delete accounts
class SerializerAccounts(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['last_login', 'groups', 'user_permissions']
        read_only_fields = ['date_joined', 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data: dict):
            create_user = Account.objects.create_user(**validate_data)
            return create_user

class SerializerUpdateAccounts(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['last_login', 'groups', 'user_permissions', "id", "is_superuser", "is_staff", "is_active" ]
        read_only_fields  = ['date_joined' , 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data: dict):
            create_user = Account.objects.create_user(**validate_data)
            return create_user

class SerializerCreateCommonUserAccounts(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['last_login', 'groups', 'user_permissions', "is_superuser", "is_staff", "is_active" ]
        read_only_fields  = ['date_joined' , 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data: dict):
            create_user = Account.objects.create_user(**validate_data)
            return create_user

#criação de funcionário
class SerializerEmployee(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['last_login', 'groups', 'user_permissions' ]
        read_only_fields  = ['date_joined' , 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}, "is_staff":{'default':True}}

    def create(self, validate_data: dict):
        create_user = Account.objects.create_user(**validate_data)
        return create_user


#update common user to staff or admin
class UpgradeToAdminOrStaff(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['is_superuser', 'is_staff']



class SerializerDeactivate(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id", "username", "is_active" ]
        extra_kwargs = {"is_active": {"required": True}, "username": {"read_only": True}, "id": {"read_only": True}}

class LoginSerializerUsername(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)
