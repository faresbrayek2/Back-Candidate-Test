from django.contrib import admin
from django.urls import path, include
from annotation import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('annotation.urls')),  # Include your app's URLs
    path('api/documents', views.document_view, name='create_document'),

]
