from django.urls import path
from . import views
app_name = 'api-v1'


urlpatterns = [
    path('list/', views.ListRequest.as_view(), name="requests-list"),
    path('superuser/list/', views.SuperUserListRequest.as_view(), name='superuser-list'),
    path('get/<int:id>/', views.GetRequest.as_view(), name="request-get"),
    path('reject/<int:pk>/', views.RejectRequest.as_view()),
    path('accept/<int:school_id>/<int:request_id>/', views.AcceptRequest.as_view()),
    path('cancel/', views.CancelRequest.as_view()),
    path('send/<int:pk>/', views.RequestForSchool.as_view(), name='request-for-school'),
    path('status/', views.StudentGetRequestStatus.as_view(), name='status'),
    path('create/<int:student_id>/<int:office_manager_id>/',views.create.as_view()),
    path('all/',views.All.as_view()),
]

