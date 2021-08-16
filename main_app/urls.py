from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('records/', views.RecordList.as_view(), name='record_list'),
    path('records/new/', views.RecordCreate.as_view(), name='record_create'),
    path('records/<int:pk>', views.RecordDetail.as_view(), name='record_detail'),
    path('records/<int:pk>/edit', views.RecordUpdate.as_view(), name='record_update'),
    path('records/<int:pk>/delete', views.RecordDelete.as_view(), name='record_delete'),
    path('records/<int:pk>/reviews/new', views.ReviewCreate.as_view(), name='review_create'),
]