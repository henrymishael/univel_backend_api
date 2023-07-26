from django.urls import path, include
from . import views
# from rest_framework.authtoken import views as drf_view
# from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('course/', views.CourseListView.as_view(), name='course'),
    path('course/<int:pk>/', views.CourseDetail.as_view(), name='course_detail'),
    path('students/', views.StudentApiView.as_view(), name='student'),
    path('students/<int:pk>/', views.StudentDetailView.as_view(), name='student_detail'),
    path('instructor/',views.InstructorListView.as_view(), name='instructor'),
    # path('user/', views.CreateNewUser.as_view(), name='new_user'),
    # path('token_login/', obtain_auth_token, name='token_login')
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

