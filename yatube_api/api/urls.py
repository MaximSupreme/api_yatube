from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import views

# from posts.views import PostViewSet, GroupViewSet, CommentViewSet


# router = DefaultRouter()
# router.register('api/v1/posts', PostViewSet, basename='post')
# router.register('api/v1/groups', GroupViewSet, basename='group')
# router.register('api/vi/posts/<int:pk>/comments', CommentViewSet, basename='comment')



urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    # path('', include(router.urls)),
    # path('api/v1/groups/', ReadOnlyModelViewSet.as_view(queryset=Group.objects.all(), serializer_class=GroupSerializer)),
    # path('api/v1/groups/<int:group_id>/', ReadOnlyModelViewSet.as_view(queryset=Group.objects.all(), serializer_class=GroupSerializer)),
    # path('api/v1/posts/<int:post_id>/comments/'),
    # path('api/v1/posts/<int:post_id>/comments/<int:comment_id>/'),
]
