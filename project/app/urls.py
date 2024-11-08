from django.urls import path
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns =[
    path('',views.index, name="index"),
    path('create/',views.create, name="create"),
    path('r/',views.retrieve,name="retrieve"),
    path('update/<int:id>',views.update,name="update"),
    path('edit/<int:id>',views.edit,name="edit"),
    path('delete/<int:id>',views.delete,name="delete"),
]

if settings.DEBUG:   
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
