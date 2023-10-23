from django.urls import path
from .views import AttendanceListView, AttendanceDetailView, AttendanceCreateView, AttendanceUpdateView, AttendanceDeleteView


urlpatterns = [
    path('<int:pk>/edit/',AttendanceUpdateView.as_view(), name='attendance_edit'), # new
    path('new/', AttendanceCreateView.as_view(), name='attendance_new'),
    path('<int:pk>/', AttendanceDetailView.as_view(), name='attendance_detail'),
    path('<int:pk>/delete/',AttendanceDeleteView.as_view(), name='attendance_delete'),
    path('', AttendanceListView.as_view(), name='home'),
]