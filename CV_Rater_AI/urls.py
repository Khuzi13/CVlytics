from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from CV_Rater_AI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('cv-checker/', views.cv_checker, name='cv_checker'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('result/', views.result, name='result'),
    path('contact_us/', views.contact_us, name='contact_us'),
]

# MEDIA files (development only)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
