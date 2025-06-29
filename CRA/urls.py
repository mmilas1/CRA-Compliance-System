from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from assessment.views import home_view  
from assessment import views as assessment_views
from assessment.views import (
    home_view,
    information_view,
    dashboard_view,
    assessment_view,
    vulnerability_assessment_view,
    redirect_after_login_view,
    annex2_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', home_view, name='home'),
    path('information/', information_view, name='information'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('assessment/', assessment_view, name='assessment_form'),
    path('login/', login_view, name='login'),
    path('assessment/class1/', assessment_view, name='assessment_class1'),
    path('assessment/vuln/', vulnerability_assessment_view, name='assessment_vuln'),
    path('redirect-after-login/', redirect_after_login_view, name='redirect_after_login'),
    path('assessment/annex2/', annex2_view, name='assessment_annex2'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]