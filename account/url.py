from django.urls import path
from account.views import login_account, register_account
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login',login_account,name="accountLogin"),
    path('logout',LogoutView.as_view(template_name="account/logout.html"),name="accountLogout"),
    path('registrar',register_account,name="accountRegistrar"),
]