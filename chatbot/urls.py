from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_ui, name='chatbot_ui'),
    path('query/', views.query_bot, name='query_bot'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('history/', views.chat_history, name='chat_history'),  
]
