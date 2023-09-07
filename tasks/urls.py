from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views


urlpatterns = [
    path("tasks/", views.TasksList.as_view()),
    path("tasks/<int:pk>/", views.TasksDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
