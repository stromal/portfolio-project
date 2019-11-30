from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs1, name='allblogs2'),
    path('<int:blog_id>/', views.detail, name='detail1'),
#   path('URL NAME THAT YOU TYPE IN to BROWSER/', include('APP FOLDER NAME.urls')),
]
