from django.urls import path, include
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
  
   path('profile/', views.profile, name='profile'),

   path('produitAV/', views.produitAV, name='produitAV'),
   path('etablirCommandeAV/', views.etablirCommandeAV, name='etablirCommandeAV'),
   path('mesCmdsAV/', views.mesCmdsAV, name='mesCmdsAV'),
   path('réclamation/', views.réclamation, name='réclamation'),


    path('update_cmdav/<int:pk>', views.update_cmdav, name='update_cmdav'),
    path('delete_cmdav/<int:pk>', views.delete_cmdav, name='delete_cmdav'),
    path('update_cmd/<int:pk>', views.update_cmd, name='update_cmd'),
    path('delete_cmd/<int:pk>', views.delete_cmd, name='delete_cmd'),


   path('payementAV/<int:pk>', views.payementAV, name='payementAV'),
   path('payementAV/payement_CompletedAV', views.payement_CompletedAV, name='payement_CompletedAV'),

   path('payementMR/<int:pk>', views.payementMR, name='payementMR'),
   path('payementMR/payement_CompletedMR', views.payement_CompletedMR, name='payement_CompletedMR'),

  path('bon_cmdAV/<int:pk>', views.bon_cmdAV, name='bon_cmdAV'),
  path('bon_cmdMR/<int:pk>', views.bon_cmdMR, name='bon_cmdMR'),
  path('render_pdf_view', views.render_pdf_view, name='render_pdf_view'),


   path('password_reset/',auth_views.PasswordResetView.as_view(template_name= 'User_AVM/password_reset_form.html'),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name= 'User_AVM/password_reset_done.html'),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name= 'User_AVM/password_reset_confirm.html'),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name= 'User_AVM/password_reset_complete.html'),name='password_reset_complete'),


   path('modifier_mdps/', views.modifier_mdps, name='modifier_mdps'),
   path('sitelivAV/', views.sitelivAV, name='sitelivAV'),


   path('loginAV/', views.loginAV, name='loginAV'),
   path('logout/' ,views.userLogout, name="logout"),


   path('', include('django.contrib.auth.urls')) ,
  # path('userProfileAV/', views.userProfileAV, name='userProfileAV'),

]

