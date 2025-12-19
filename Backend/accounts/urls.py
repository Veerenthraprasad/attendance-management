from django.urls import path
from .views import (
    MeView,
    CreateUserView,
    ListUsersView,
    UpdateUserView,
    DeactivateUserView,
)

urlpatterns = [
    path("me/", MeView.as_view()),
    path("create/", CreateUserView.as_view()),
    path("list/", ListUsersView.as_view()),
    path("update/<int:pk>/", UpdateUserView.as_view()),
    path("deactivate/<int:pk>/", DeactivateUserView.as_view()),
]
