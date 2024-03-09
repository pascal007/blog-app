from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView, PostViewSet,
)

router = DefaultRouter()
router.register(r'', PostViewSet)

urlpatterns = [
    path('post', PostListView.as_view(), name='post_list'),
    path('post/<uuid:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<uuid:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<uuid:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

urlpatterns += [
    path('api/v1/post/', include(router.urls)),
]