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


# Login com username, email ou telefone

from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.views import Request, Response
from django.shortcuts import get_object_or_404
from .serializers import LoginSerializerUsername
from django.contrib.auth import authenticate

class LoginAccount(views.ObtainAuthToken):

    def post(self, request: Request) -> Response:
        user_dict = request.data

        if request.data.get('email'):
            username = get_object_or_404(Account, email=request.data['email']).username
            user_dict['username'] = username

        elif request.data.get('cellphone'):
            username = get_object_or_404(Account, cellphone=request.data['cellphone']).username
            user_dict['username'] = username

        serializer = LoginSerializerUsername(data=user_dict)
        serializer.is_valid(raise_exception=True)
        login_user = authenticate(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=login_user)
        return Response({"token": token.key})