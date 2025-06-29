# Handles routes for the CRA form
from django.urls import path
from assessment.views import (  
    dashboard_view,
    information_view,
    assessment_view,
    vulnerability_assessment_view,
    redirect_after_login_view,
    annex2_view,
    home_view
)

urlpatterns = [
    path('', home_view, name='home'),
    path('information/', information_view, name='information'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('assessment/', assessment_view, name='assessment_form'),
    path('assessment/class1/', assessment_view, name='assessment_class1'),
    path('assessment/vuln/', vulnerability_assessment_view, name='assessment_vuln'),
    path('redirect-after-login/', redirect_after_login_view, name='redirect_after_login'),
    path('assessment/annex2/', annex2_view, name='assessment_annex2'),
]
