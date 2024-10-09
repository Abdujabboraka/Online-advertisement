from django.urls import path
from .views import homepage, select_by_category, add_post, all_posts, view_more
urlpatterns = [
    path('', homepage, name='homepage'),
    path('category/<category_id>/', select_by_category, name='categories'),
    path('add_post', add_post, name='add_post'),
    path('all_posts', all_posts, name='all_posts'),
    path('view_more/<ad_id>', view_more, name='view_more'),  # Add new URL for view_more view.
]