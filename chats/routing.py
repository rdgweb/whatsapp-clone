from django.urls import path , include
from chats.consumers import PersonalChatConsumer, NotificationConsumer, OnlineStatusConsumer
 
# Here, "" is routing to the URL ChatConsumer which
# will handle the chat functionality.
websocket_urlpatterns = [
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
    path('ws/online/', OnlineStatusConsumer.as_asgi()),
    path('ws/notify/', NotificationConsumer.as_asgi())
]