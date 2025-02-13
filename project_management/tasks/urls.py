from django.urls import path
from tasks import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('category/', views.CategoryList.as_view(), name='category-list'),
    path('category/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    path('categories/<int:category_id>/add-tasks', views.AddTasksToCategory.as_view(), name='add-tasks-to-category')
]


#should i include it
# urlpatterns = format_suffix_patterns(urlpatterns)


















