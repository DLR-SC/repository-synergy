from django.urls import path

from . import views

app_name = "reposynergy"
urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'), # redirects the annotator to the guideline + all repos to annotate
    path('annotate/<str:pair_id>/', views.annotate, name='annotate'), # redirects to the next repo pairs - shows readme files and the questions+
    path('save_annotation', views.save_annotation, name='save_annotation'),
    path('upload_repopairs', views.upload_repopairs, name='upload_repopairs'),
    path('create_show_users', views.create_show_users, name='create_show_users'),
    path('download_annotations', views.download_annotations, name='download_annotations'),
    path('download_users', views.download_users, name='download_users'),
    path('download_repo_pairs', views.download_repo_pairs, name='download_repo_pairs'),
    path('view_annotations/<int:batch_num>/', views.view_annotations, name='view_annotations'),
    path('deactivate_user/<int:user_id>/', views.deactivate_user, name='deactivate_user'),
    path('activate_user/<int:user_id>/', views.activate_user, name='activate_user'),
    path('download_annotations_view/<int:batch_num>/', views.download_annotations_view, name='download_annotations_view'),


]