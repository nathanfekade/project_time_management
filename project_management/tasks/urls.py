from django.urls import path
from tasks import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail')
]

#should i include it
# urlpatterns = format_suffix_patterns(urlpatterns)