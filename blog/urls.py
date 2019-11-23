from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs1, name='allblogs2')
#   path('URL NAME THAT YOU TYPE IN to BROWSER/', include('APP FOLDER NAME.urls')),
]
