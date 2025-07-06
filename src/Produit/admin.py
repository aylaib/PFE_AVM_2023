from django.contrib import admin
from .models import *

# Register your models here.

class ProduitAv_admin(admin.ModelAdmin):
    list_display = ['id','nomP', 'prix','prixD', 'catégorie', 'image', 'prP_av']
    list_display_links = ['id','nomP']
    search_fields = ['nomP']

class ProduitMr_admin(admin.ModelAdmin):
    list_display = ['id','nomP_mr', 'prix_mr', 'prix_mrD', 'catégorie_mr', 'image_mr', 'prP_mr']
    list_display_links = ['id','nomP_mr']
    search_fields = ['nomP_mr']




admin.site.register(Catégorie)

admin.site.register(ProduitAV,ProduitAv_admin)

admin.site.register(ProduitMR,ProduitMr_admin)
