from accounts.serializers import SerializerAccounts, UpgradeToAdminOrStaff, Desactivate, SerializerEmployee
from rest_framework import generics
from .models import Account
from rest_framework.authentication import TokenAuthentication
from .permissions import UpdateAndDelete, OnlyAdmin, ReadOnlyAdmin

#Cria user comum (Não precisa de permissão), Lista todos users (apenas admin)
class AccountView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]        
    permission_classes = [ReadOnlyAdmin]
    queryset = Account.objects.all()
    serializer_class = SerializerAccounts
    
#Cria funcionario(apenas admin)
class CreateEmployee(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]        
    permission_classes = [OnlyAdmin]
    queryset = Account.objects.all()
    serializer_class = SerializerEmployee
    
# Visualiza, atualiza ou deleta user apenas se for admin ou o própio user   
class AcccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]        
    permission_classes = [UpdateAndDelete]    
    queryset = Account.objects.all()
    serializer_class = SerializerAccounts
    
# Admin atualiza qualquer user como funcionário ou admin   
class UpgradeToAdminOrStaff(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]        
    permission_classes = [OnlyAdmin]    
    queryset = Account.objects.all()
    serializer_class = UpgradeToAdminOrStaff   
    
# Admin pode desativar funcionário    
class DesactivateAccount(generics.UpdateAPIView):
    authentication_classes = [ TokenAuthentication]        
    permission_classes = [OnlyAdmin]    
    queryset = Account.objects.all()
    serializer_class = Desactivate 
    