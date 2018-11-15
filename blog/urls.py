from django.urls import path 
from blog.views import read_post, write_post, edit_read_post, get_unpublished_post, publish_post

urlpatterns = [
    path('posts/<int:id>/publish/', publish_post, name='publish_post'),
    path('unpublished_post/', get_unpublished_post, name='unpublished_post'),
    path('write_post/', write_post, name="write_post"),
    path('read_post/<int:id>', read_post, name="read_post"),
    path('edit_post/id/<int:id>', edit_read_post, name="edit_post"),
    
]