from django.urls import path
from . import views

app_name = 'club'

urlpatterns = [
    path('index/', views.index, name='index'),

    path('about_detail/<int:id>', views.about_detail_def, name="about_detail_url"),

    path('member_list', views.MemberListView.as_view(), name="member_list_url"),
    path('member_detail/<int:id>', views.member_detail_def, name="member_detail_url"),

    path('field_list', views.FieldListView.as_view(), name="field_list_url"),
    path('field_detail/<int:id>', views.field_detail_def, name="field_detail_url"),

]
