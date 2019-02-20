

from django.urls import path
from . import home
urlpatterns = [
    path('', home.homepage),
     path('count/', home.count,name='count'),
]
