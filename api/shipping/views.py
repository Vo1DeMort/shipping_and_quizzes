from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import (
    CustomTokenObtainPairSerializer,
    RegisterSerializer,
    PackageSerializer,
    PkgSerializer,
)
from rest_framework import generics
from .models import CustomUser, Package
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.db.models import Q


# login with username and password
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

    """
class CreateListShipping(generics.ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Package
    serializer_class= PackageSerializer

class (generics.RetrieveDestroyAPIView):
    permission_classes=[IsAuthenticated]
    queryset = Package
    serializer_class= PackageSerializer

"""


# retrieveupdate destropview
# normal user access - create -update- get
# admin user access - list,delete


class CreatePkg(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Package.objects.all()
    serializer_class = PkgSerializer


# get the login user's shipping list,send or recieve
class ListPkg(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageSerializer

    def get_queryset(self):
        user = self.request.user
        return Package.objects.filter(sender=user) | Package.objects.filter(
            receiver=user
        )


class UpdatePkgStatus(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PackageSerializer

    def get_queryset(self):
        user = self.request.user
        # get only the pkg that current user is about to recieve
        # and current user can change the status to done as a sign of good recieve
        return Package.objects.filter(receiver=user, status="on")


class DeletePkg(generics.DestroyAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = PackageSerializer
    queryset = Package.objects.all()


# need a user search view to send the front end back user ids
# /users/search/?email_or_username=${emailOrUsername}
class UserSearchView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        email_or_username = request.query_params.get("email_or_username")
        try:
            user = CustomUser.objects.get(
                Q(email=email_or_username) | Q(username=email_or_username)
            )
            return Response({"id": user.id})
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found"}, status=404)
