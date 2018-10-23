from django.urls import path
from .import views
app_name='music'
urlpatterns = [
    # /music1
    path('', views.IndexView.as_view(), name='index'),
    #register
    path('register/', views.UserFormView.as_view(), name='register'),

    #/music/albumid
    path('<pk>/', views.DetailsView.as_view(), name='details'),

    #music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='album-add'),

    # music/album/update
    path('album/<pk>/', views.AlbumUpdate.as_view(), name='album-update'),
    # music/album/add
    path('album/<pk>/delete/', views.AlbumDelete.as_view(), name='album-delete'),

]