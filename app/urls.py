from django.urls import path
from .views import *


urlpatterns = [
    path('list/', TodoAppView.as_view(), name='todo-list'),
    path('completed/', TodoCompletedView.as_view(), name='todo-completed'),
    

]
