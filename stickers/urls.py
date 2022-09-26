from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stickers import views

# Create your views here.
urlpatterns = [
    path('stickers/', views.StickerList.as_view(), name="all-stickers"),
    path('stickers/<int:pk>/', views.StickerDetail.as_view(), name='sticker-detail'),
    path('users/', views.UserList.as_view(), name="all-users"),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='profile-detail'),
    path('user/<int:pk>/stickers/',
         views.UserStickerList.as_view(), name='user-sticker'),
    # may need to use the userpk inbetween
    path('user/follow/', views.FollowCreate.as_view(), name='follow-user'),
    path('following/', views.FollowingList.as_view(), name="following-users"),
    path('followed-by/', views.FollowedList.as_view(), name="followed-by-users"),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
