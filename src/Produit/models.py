from django.db import models

# Create your models here.


NC = (
    ('Aviation', 'Aviation'),
    ('Marine','Marine')
)

class Catégorie(models.Model):
    nomC = models.CharField(max_length=50 ,verbose_name=('Catégorie'), choices=NC)


    def __str__(self):
        return self.nomC
  
  
class ProduitAV(models.Model):
    nomP = models.CharField(max_length=50, verbose_name=("Produit"))
    prix = models.FloatField(default=0, verbose_name=("Prix (Dinar)"))
    prixD = models.FloatField(default=0, verbose_name=("Prix (Dollar)"))
    catégorie = models.ForeignKey(Catégorie, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000, default='', blank=True, null=True)
    image = models.ImageField(blank=True , null=True)
    prP_av = models.FloatField(default=None, blank=True, null=True, verbose_name=("Promotion"))



    def __str__(self):
        return self.nomP
    

    @staticmethod
    def get_all_productsAV():
        return ProduitAV.objects.all()
    
    @staticmethod
    def get_nbr_productsAV():
        return ProduitAV.objects.count()
    

    



class ProduitMR(models.Model):
    nomP_mr = models.CharField(max_length=50, verbose_name=("Produit"))
    prix_mr = models.FloatField(default=0, verbose_name=("Prix (Dinar)"))
    prix_mrD = models.FloatField(default=0, verbose_name=("Prix (Dollar)"))
    catégorie_mr = models.ForeignKey(Catégorie, on_delete=models.CASCADE, verbose_name=("catégorie"))
    description_mr = models.CharField(max_length=1000, default='', blank=True, null=True, verbose_name=("description"))
    image_mr = models.ImageField(blank=True , null=True, verbose_name=("image"))
    prP_mr = models.FloatField(default=None, blank=True, null=True, verbose_name=("Promotion"))
        


    def __str__(self):
        return self.nomP_mr
    

    @staticmethod
    def get_all_productsMR():
        return ProduitMR.objects.all()
    
    @staticmethod
    def get_nbr_productsMR():
        return ProduitMR.objects.count()
    








