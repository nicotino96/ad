"""
URL configuration for IdeAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from idearest25app import endpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/health', endpoints.health_check),
    path('v1/users', endpoints.users),
    path('v1/sessions', endpoints.sessions),
    path('v1/categories', endpoints.categories),
    path('v1/categories/<int:category_id>/ideas', endpoints.ideas),
    path('v1/ideas/<int:idea_id>/comments', endpoints.comments),
]
