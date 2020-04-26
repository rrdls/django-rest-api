from django.urls import path
from register import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:id>', views.UserDetail.as_view())
]
