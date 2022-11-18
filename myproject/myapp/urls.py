from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from myapp.views import register_view
from myapp import views

urlpatterns = [
    path('',views.index, name=''),
    path('view/',views.view_list,name='view'),
    path('register/',register_view, name = 'register'),
    path('post/',views.Post_view.as_view(),name ='post'),
   
]

if settings.DEBUG:

    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)