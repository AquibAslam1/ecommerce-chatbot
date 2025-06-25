from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chatbot/', include('chatbot.urls')),

    # 👇 Add this line to include your custom signup route
    path('accounts/', include('accounts.urls')),

    # Built-in auth views (login, logout, password reset, etc.)
    path('accounts/', include('django.contrib.auth.urls')),

    # Redirect root "/" to login page
    path('', lambda request: redirect('login')),
]
