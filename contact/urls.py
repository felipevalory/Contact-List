from django.contrib import admin
from django.urls import path
from contact import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'contact'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),

    # Contact (CRUD)
    path('contact/<int:contact_id>/detail/', views.contact, name='contact'),
    path('contact/create/', views.create, name='create'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
