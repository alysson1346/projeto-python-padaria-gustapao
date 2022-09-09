from accounts.serializers import SerializerAccounts, SerializerCreateCommonUserAccounts, SerializerDeactivate, SerializerUpdateAccounts, UpgradeToAdminOrStaff, SerializerEmployee
from rest_framework import generics
from .models import Account
from rest_framework.authentication import TokenAuthentication
from utils.mixins import SerializerByMethodMixin
from .permissions import UpdateAndDelete, OnlyAdmin, ReadOnlyAdmin


#Cria user comum (Não precisa de permissão), Lista todos users (apenas admin)

class AccountView(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [ReadOnlyAdmin]
    queryset = Account.objects.all()

    serializer_map = {
        'GET': SerializerAccounts,
        'POST': SerializerCreateCommonUserAccounts,
    }

#Cria funcionario(apenas admin)
class CreateEmployee(SerializerByMethodMixin, generics.ListCreateAPIView):
    permission_classes = [OnlyAdmin]

    queryset = Account.objects.filter(is_staff=True)
    serializer_map = {
        'GET': SerializerEmployee,
        'POST': SerializerEmployee,
    }


# Visualiza, atualiza ou deleta user apenas se for admin ou o própio user
class AcccountDetailView(SerializerByMethodMixin, generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [UpdateAndDelete]

    queryset = Account.objects.all()
    serializer_map = {
        'GET': SerializerAccounts,
        'PATCH': SerializerUpdateAccounts,
        'DELETE': SerializerAccounts,
    }

# Admin atualiza qualquer user como funcionário ou admin
class UpgradeToAdminOrStaff(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [OnlyAdmin]

    queryset = Account.objects.all()
    serializer_map = {
        'PATCH': UpgradeToAdminOrStaff
    }


# Admin pode desativar funcionário
class DeactivateAccountView(SerializerByMethodMixin, generics.UpdateAPIView):
    authentication_classes = [ TokenAuthentication]
    permission_classes = [OnlyAdmin]

    queryset = Account.objects.all()
    serializer_map = {
        'PATCH': SerializerDeactivate
    }
