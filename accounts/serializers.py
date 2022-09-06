from statistics import mode
from rest_framework import serializers
from .models import Account

class SerializerAccounts(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['last_login', 'groups', 'user_permissions' ]
        read_only_fields  = ['date_joined' , 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validate_data: dict):
            create_user = Account.objects.create_user(**validate_data)
            return create_user
        
class SerializerEmployee(serializers.ModelSerializer):
    class Meta:
        model = Account
        exclude = ['last_login', 'groups', 'user_permissions' ]
        read_only_fields  = ['date_joined' , 'is_active', 'is_superuser']
        extra_kwargs = {'password': {'write_only': True}, "is_staff":{'required':True}}
        
    
    def create(self, validate_data: dict):
            create_user = Account.objects.create_user(**validate_data)
            return create_user

class UpgradeToAdminOrStaff(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['is_superuser', 'is_staff' ]
 
        
class Desactivate(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['is_active']

        
        

