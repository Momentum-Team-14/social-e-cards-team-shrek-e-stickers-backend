from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stickers import views

# Create your views here.
urlpatterns = [
    path('stickers/', views.StickerList.as_view(), name="all-stickers"),
    path('stickers/<int:pk>/', views.StickerDetail.as_view(), name='sticker-detail'),
    path('users/', views.UserList.as_view(), name="all-users"),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='profile-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
