from django.urls import path
from . import views

urlpatterns = [
    
    path('finance/structure/', views.structure_loan, name='structure_loan'),
    path('finance/structure-loan/', views.structure_loan, name='structure_loan_alias'),
    path('structure-loan/', views.structure_loan, name='structure_loan_flat'),

     
    path('competitors/density/', views.competitors_density, name='competitors_density'),
    path('competitors-density/', views.competitors_density, name='competitors_density_flat'),
    path('geo/competitors-density/', views.competitors_density, name='competitors_density_alias'),

     
    path('feasibility/generate/', views.generate_feasibility, name='generate_feasibility'),
    path('feasibility/', views.generate_feasibility, name='generate_feasibility_flat'),
    path('ai/feasibility-study/', views.generate_feasibility, name='feasibility_study_alias'),

    
    path('feasibility/evaluate/', views.full_feasibility_evaluation, name='full_feasibility_evaluation'),
    path('feasibility-evaluate/', views.full_feasibility_evaluation, name='full_feasibility_evaluation_flat'),
    path('analysis/full-evaluation/', views.full_feasibility_evaluation, name='analysis_full_evaluation_alias'),

     
    path('auth/otp-login/', views.otp_login, name='otp_login'),
    path('otp-login/', views.otp_login, name='otp_login_flat'),
]