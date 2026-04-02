from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import login_page, register_page, jobs_page, home, dashboard,post_job

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # API Routes
    path('api/auth/', include('accounts.urls')),
    path('api/jobs/', include('jobs.urls')),
    path('api/applications/', include('applications.urls')),

    # Frontend Pages
    path('', home, name='home'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('jobs/', jobs_page, name='jobs'),
    path('dashboard/', dashboard, name='dashboard'),
    path('post-job/', post_job, name='post_job'),
]

# Serve media files (ONLY in development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)