from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    RegisterView,
    CreatePkg,
    ListPkg,
    UpdatePkgStatus,
    DeletePkg,
    UserSearchView,
)
from drf_spectacular.views import SpectacularRedocView

urlpatterns = [
    # auth
    path("register/", RegisterView.as_view()),
    path("login/", CustomTokenObtainPairView.as_view()),
    # CRUD
    path("create-pkg/", CreatePkg.as_view()),
    path("list-pkg/", ListPkg.as_view()),
    path("update-pkg-stat/<int:pk>/", UpdatePkgStatus.as_view()),
    path("delete-pkg/<int:pk>/", DeletePkg.as_view()),
    # search user by username or email
    path("search/", UserSearchView.as_view()),
    # redoc
    path("schema/redoc/", SpectacularRedocView.as_view()),
]
