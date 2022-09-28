from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from stickers import views

# Create your views here.
urlpatterns = [
    path('stickers/', views.StickerList.as_view(), name="all-stickers"),
    path('stickers/<int:pk>/', views.StickerDetail.as_view(), name='sticker-detail'),
    path('users/', views.UserList.as_view(), name="all-users"),
    path('myprofile/', views.UserProfile.as_view(), name='my-profile'),
    path('profile/<int:pk>/', views.UserDetail.as_view(), name='profile-detail'),
    path('user/<int:pk>/stickers/',
         views.UserStickerList.as_view(), name='user-sticker'),
    path('mystickers/', views.UserStickerList.as_view(), name='my-stickers'),
    path('user/<int:pk>/follow/', views.FollowCreate.as_view(), name='follow-user'),
    path('user/<int:pk>/unfollow/',
         views.UnFollowDestroy.as_view(), name='unfollow-user'),
    path('following/', views.FollowingList.as_view(), name="following-users"),
    path('followers/', views.FollowedByList.as_view(), name="followers"),
    path('', views.api_root),
    path('stickers/following/', views.FollowListStickers.as_view(),
         name="follow-stickers"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
