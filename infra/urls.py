from django.urls import path
from .import views
from .views import file_upload, file_upload_success
from .views import photo_list, photo_upload, selected_photos, panorama_list, panorama_upload
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index_view, name='index'),
    path('article/<int:pk>/infra/', views.ListInfraView.as_view(), name='list-infra'),
    path('article/<int:pk>/infra/create/', views.CreateInfraView.as_view(), name='create-infra'),
    path('article/<int:pk>/infra/detail/', views.DetailInfraView.as_view(), name='detail-infra'),
    path('article/<int:pk>/infra/delete/', views.DeleteInfraView.as_view(), name='delete-infra'),
    path('article/<int:pk>/infra/update/', views.UpdateInfraView.as_view(), name='update-infra'),
    path('article/', views.ListArticleView.as_view(), name='list-article'),
    path('article/create/', views.CreateArticleView.as_view(), name='create-article'),
    path('article/<int:pk>/detail/', views.DetailArticleView.as_view(), name='detail-article'),
    path('article/<int:pk>/delete/', views.DeleteArticleView.as_view(), name='delete-article'),
    path('article/<int:pk>/update/', views.UpdateArticleView.as_view(), name='update-article'),
    path('upload/', views.file_upload, name='file_upload'),
    path('upload/success/', views.file_upload_success, name='file_upload_success'),
    path('photos/', views.photo_list, name='photo_list'),
    path('photos/upload/', views.photo_upload, name='photo_upload'),
    path('photos/selected/', views.selected_photos, name='selected_photos'),
    path('panorama/list/', views.panorama_list, name='panorama_list'),
    path('images/', views.image_list, name='image_list'),# 全景写真
    path('photo/', views.display_photo, name='photo'),# 全景写真のアップロード
    path('table/', views.table_view, name='table'),# 損傷写真帳
    path('number/', views.number_create_view, name='number'),
    path('ajax-file-send/', views.ajax_file_send, name='ajax_file_send'),# 損傷写真帳の写真変更
]
# path('URLの末尾', views.py内の関数名(操作に対するリクエストを受ける), ルーティングに名前を付ける(この名前でURLを参照できるようになる)),
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)