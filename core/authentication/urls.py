from django.urls import path
from .views import LonginView, SignUpView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignUpView.as_view())
]