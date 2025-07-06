from django.forms import ModelForm

from .models import *



##################### Client Form ###########################


class ClientForm(ModelForm):
    class Meta:
        model = ClientAv
        fields = ['user_nameAV', 'email', 'phone', 'pays', 'avatar']




##################### Commande Aviation Form ###########################



class CommandeAVForm(ModelForm):
    class Meta:
        model = CommandeAv
        fields = ['produit','quantity','site_Livraison_Aviation', 'type_deviseAv']





##################### Commande Marine Form ###########################




class CommandeMRForm(ModelForm):
    class Meta:
        model = CommandeMr
        fields = ['produitmr','quantitymr','site_Livraison_Marine', 'type_deviseMr']