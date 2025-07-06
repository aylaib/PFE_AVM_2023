from django.db import models

# Create your models here.
from django.db import models
import datetime

from Produit.models import *
from django.contrib.auth.models import User

# Create your models here.
  
typeCl = (
    ('Aviation', 'Aviation'),
    ('Marine','Marine')
)

typeDv = (
    ('DA', 'DA'),
    ('$','$')
)

class ClientAv(models.Model):
    user = models.OneToOneField(User,null=True ,on_delete=models.CASCADE)
    CodeClient = models.CharField(max_length=50, unique=True, null=True)
    user_nameAV = models.CharField(max_length=50, verbose_name=("nom d'utilisateur"))
    type_client = models.CharField(max_length=30, null=True,choices=typeCl)
    phone = models.CharField(max_length=10, verbose_name=("num telephone"))
    email = models.EmailField(max_length=30)
    pays = models.CharField(max_length=40, null=True)
    avatar = models.ImageField(blank=True , null=True, default='images/img/kisspng-logo-person-user-person-icon-5b4d2bd1eadf26.611780081531784145962.jpg')

    def __str__(self):
        return self.user.username





class SiteLiv_AV(models.Model):
    Nom_SiteAV = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Nom_SiteAV

  
class CommandeAv(models.Model):

    clientAV = models.ForeignKey(ClientAv,
                                 on_delete=models.CASCADE, verbose_name=("client"))
    produit = models.ForeignKey(ProduitAV,
                                on_delete=models.CASCADE,)
    quantity = models.IntegerField(verbose_name=("quantité"))
    price = models.FloatField(verbose_name=("prix total"))
    site_Livraison_Aviation = models.ForeignKey(SiteLiv_AV, on_delete=models.CASCADE)
    type_deviseAv = models.CharField(max_length=10, null=True,choices=typeDv, verbose_name=("type devise"))
    date = models.DateField(default=datetime.datetime.today, verbose_name=("date recu commande"))
    Confirmer_Commande= models.BooleanField(default=False)
    Annuler_Commande = models.BooleanField(default=False)
    etat_payementav = models.BooleanField(blank=True,default=False, verbose_name=("etat payement"))
    date_Livraison_av = models.DateField(null=True,blank=True ,verbose_name=("date livrason"),help_text='Please enter the date in <em>YYYY-MM-DD</em> format.')

    
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'Commande numéro {self.id} établie par {self.clientAV.user_nameAV} :'
 





class SiteLiv_MR(models.Model):
    Nom_SiteMR = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Nom_SiteMR


  
class CommandeMr(models.Model):

    client = models.ForeignKey(ClientAv,
                                 on_delete=models.CASCADE)
    produitmr = models.ForeignKey(ProduitMR,
                                on_delete=models.CASCADE, verbose_name=("produit"))
    quantitymr = models.IntegerField(verbose_name=("quantité"))
    pricemr = models.FloatField(verbose_name=("prix total"))
    site_Livraison_Marine = models.ForeignKey(SiteLiv_MR, on_delete=models.CASCADE)
    type_deviseMr = models.CharField(max_length=10, null=True ,choices=typeDv, verbose_name=("type devise"))
    dateC = models.DateField(default=datetime.datetime.today, verbose_name=("date recu commande"))
    Confirmer_Commande_mr= models.BooleanField(default=False,verbose_name=("Confirmer Commande"))
    Annuler_Commande_mr = models.BooleanField(default=False, verbose_name=("Annuler Commande"))
    etat_payementmr = models.BooleanField(blank=True,default=False, verbose_name=("etat payement"))
    date_Livraison_mr = models.DateField(null=True,blank=True ,verbose_name=("date livraison"))



    def __str__(self):
        return f'Commande numéro {self.id} établie par {self.client.user_nameAV} :'

   



class Reclamation(models.Model):

    clientRc = models.CharField(max_length=30,verbose_name=("Nom Client"))
    emailCl = models.EmailField(max_length=50, verbose_name=("Email Client")) 
    sujet = models.CharField(max_length=100)
    message = models.CharField(max_length=1500)
    dateRec = models.DateField(default=datetime.datetime.today, verbose_name=("date recu reclamation"))
  



    def __str__(self):
        return f'Réclamation numéro {self.id} a la part de {self.clientRc}'