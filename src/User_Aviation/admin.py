from django.contrib import admin
from .models import * 


# Register your models here.


class Client_admin(admin.ModelAdmin):
    list_display = ['CodeClient','user_nameAV', 'type_client', 'phone', 'email' ,'pays' ,'avatar']
    list_display_links = ['CodeClient','user_nameAV']
    search_fields = ['CodeClient','user_nameAV']
    list_filter = ['type_client']


class CommandeAv_admin(admin.ModelAdmin):
    list_display = ['id','clientAV', 'produit', 'quantity', 'price', 'type_deviseAv','site_Livraison_Aviation', 'date', 'Confirmer_Commande', 'Annuler_Commande' ,'etat_payementav','date_Livraison_av']
    readonly_fields = ['id','clientAV', 'produit', 'quantity', 'price','type_deviseAv', 'site_Livraison_Aviation', 'date','etat_payementav']
    list_display_links = ['id','clientAV']
    search_fields = ['id']
    list_filter = ['Confirmer_Commande']
    

class CommandeMr_admin(admin.ModelAdmin):
    list_display = ['id','client', 'produitmr', 'quantitymr', 'pricemr', 'type_deviseMr','site_Livraison_Marine' ,'dateC',  'Confirmer_Commande_mr', 'Annuler_Commande_mr', 'etat_payementmr','date_Livraison_mr']
    readonly_fields = ['id','client', 'produitmr', 'quantitymr', 'pricemr','type_deviseMr', 'site_Livraison_Marine', 'dateC','etat_payementmr']
    list_display_links = ['id','client']
    search_fields = ['id']
    list_filter = ['Confirmer_Commande_mr']


class Reclamation_admin(admin.ModelAdmin):
    readonly_fields = ['clientRc', 'emailCl', 'sujet', 'message', 'dateRec']
    search_fields = ['id']
    

   

admin.site.register(ClientAv, Client_admin)

admin.site.register(SiteLiv_AV)

admin.site.register(SiteLiv_MR)

admin.site.register(CommandeAv,CommandeAv_admin)

admin.site.register(CommandeMr,CommandeMr_admin)


admin.site.register(Reclamation,Reclamation_admin)
