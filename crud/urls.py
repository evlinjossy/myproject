from django.urls import path
from .views import studentList, studentDetail
urlpatterns = [
    path('students/', studentList.as_view(), name='student-list'),
    path('students/<int:id>/', studentDetail.as_view(), name='student-detail'),
]