from django.urls import path,re_path
from app import views
app_name = 'app'
urlpatterns = [
    path('infoupload',views.InfoUpload.as_view()),
]