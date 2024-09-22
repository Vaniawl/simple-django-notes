from django.urls import path
from .views import send_content, read_content, update_content, delete_content, special_page, index, note_detail, delete




urlpatterns = [
    path('send/', send_content),
    path('read/', read_content),
    path('update/', update_content),
    path('delete/', delete_content),
    # path('', your_view_function, name='notes'),
    path('', index, name='notes'),
    path('note/<int:note_id>/', note_detail, name='note_detail'),
    path('note/<int:note_id>/delete/', delete, name='delete'),
]


