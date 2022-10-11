
from django.contrib.auth import authenticate
from .serializers import LoginSerializerUsername
from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, APIView
from rest_framework.authtoken.models import Token
from accounts.serializers import SerializerAccounts, SerializerCreateCommonUserAccounts, SerializerDeactivate, SerializerUpdateAccounts, UpgradeToAdminOrStaff, SerializerEmployee

from rest_framework import generics
from .models import Account
from rest_framework.authentication import TokenAuthentication
from utils.mixins import SerializerByMethodMixin
from .permissions import UpdateAndDelete, OnlyAdmin, ReadOnlyAdmin
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from rest_framework.views import Request, Response
from django.shortcuts import get_object_or_404
from .serializers import LoginSerializerUsername
from django.contrib.auth import authenticate



#Cria user comum (Não precisa de permissão), Lista todos users (apenas admin)

class AccountView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [ReadOnlyAdmin]
    queryset = Account.objects.all()
    serializer_class = SerializerAccounts
    serializer_map = {
        'GET': SerializerAccounts,
        'POST': SerializerCreateCommonUserAccounts,
    }

#Cria funcionario(apenas admin)
class CreateEmployee(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [OnlyAdmin]

    queryset = Account.objects.filter(is_staff=True)
    serializer_class = SerializerEmployee
    serializer_map = {
        'GET': SerializerEmployee,
        'POST': SerializerEmployee,
    }


# Visualiza, atualiza ou deleta user apenas se for admin ou o própio user
class AcccountDetailView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [UpdateAndDelete]

    queryset = Account.objects.all()
    serializer_class = SerializerAccounts,
    serializer_map = {
        'GET': SerializerAccounts,
        'PATCH': SerializerUpdateAccounts,
        'DELETE': SerializerAccounts,
    }

# Admin atualiza qualquer user como funcionário ou admin
class UpgradeToAdminOrStaff(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyAdmin]

    serializer_class = UpgradeToAdminOrStaff
    queryset = Account.objects.all()
    serializer_map = {
        'PATCH': UpgradeToAdminOrStaff
    }


# Admin pode desativar funcionário
class DeactivateAccountView(SerializerByMethodMixin, generics.UpdateAPIView):
    permission_classes = [OnlyAdmin]

    serializer_class = SerializerDeactivate
    queryset = Account.objects.all()
    serializer_map = {
        'PATCH': SerializerDeactivate
    }

# Login com username, email ou telefone

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
        
# Admin pode desativar funcionário    
class DesactivateAccount(generics.UpdateAPIView):
    authentication_classes = [ TokenAuthentication]        
    permission_classes = [OnlyAdmin]    
    queryset = Account.objects.all()
    serializer_class = SerializerDeactivate 

# Login com username, email ou telefone
class LoginAccount(APIView):

    def post(self, request: Request) -> Response:
        user_dict = request.data

        if request.data.get('email'):
            username = get_object_or_404(
            Account, email=request.data['email']).username
            user_dict['username'] = username

        elif request.data.get('cellphone'):
            username = get_object_or_404(
            Account, cellphone=request.data['cellphone']).username
            user_dict['username'] = username

        serializer = LoginSerializerUsername(data=user_dict)
        serializer.is_valid(raise_exception=True)
        login_user = authenticate(**serializer.validated_data)
        token, _ = Token.objects.get_or_create(user=login_user)
        return Response({"token": token.key})

	