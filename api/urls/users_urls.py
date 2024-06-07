from django.urls import path
from users import views as users_view

urlpatterns = [
    path('register/', users_view.registerUser, name='register'),
    path('profile/', users_view.getUserProfile, name="user-profile"),
    path('profile/update/', users_view.updateUserProfile, name="user-profile-update"),
    path('login/', users_view.MyTokenObtainPairView.as_view(), name='token-obtai-pair'),
    path('delete/<str:pk>/', users_view.deleteUser, name="deleteUser"),
]