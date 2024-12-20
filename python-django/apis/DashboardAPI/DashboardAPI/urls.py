"""
URL configuration for DashboardAPI project.

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

from dashboard25app import endpoints

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/dashboards', endpoints.all_dashboards),
    path('api/v1/dashboards/<int:path_param_id>/questions', endpoints.questions_from_dashboard),
    path('api/v1/questions/<int:question_id>/answers', endpoints.answers_for_questions)
]
