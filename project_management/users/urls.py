from django.urls import path
from users import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.UserList.as_view(), name='user-list'),
    path('<int:pk>', views.UserDetail.as_view(), name='user-detail')
]