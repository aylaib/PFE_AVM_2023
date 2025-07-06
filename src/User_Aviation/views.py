from django.shortcuts import render, redirect
from user_app.models import *
from Produit.models import *
from .models import *

from django.contrib import messages
from django.contrib.auth import authenticate ,login  , logout 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

from .forms import *

from .decorators import *

from django.core.mail import send_mail
from django.conf import settings



import json
from django.http import JsonResponse

from datetime import date
from django.core.paginator import Paginator

from django.db.models import Exists, OuterRef

from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa



# Create your views here.


@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def profile(request):
 
 nbrCmd_AV = request.user.clientav.commandeav_set.count() 
 nbrCmd_MR = request.user.clientav.commandemr_set.count() 
 
 client = request.user.clientav

 infoClient = ClientForm(instance=client)

 if request.method == 'POST':
     infoClient = ClientForm(request.POST, request.FILES, instance=client)
     if infoClient.is_valid():
         request.user.username = infoClient.cleaned_data['user_nameAV']
         request.user.email = infoClient.cleaned_data['email']
         request.user.save()
         infoClient.save()
            

 context = {'infoClient': infoClient, 'nbrCmd_AV': nbrCmd_AV, 'nbrCmd_MR': nbrCmd_MR }

 return render(request, 'User_AVM/profile.html', context)





########################################## Consulter Produits ############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def produitAV(request):
 
 prdAV = ProduitAV.get_all_productsAV()

 prdMR = ProduitMR.get_all_productsMR()


            

 context = {'prdAV':prdAV,
            'prdMR':prdMR,}

 return render(request, 'User_AVM/produitAV.html', context)





########################################## Etablir Commande ############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def etablirCommandeAV(request):
      prdAV = ProduitAV.get_all_productsAV()

      prdMR = ProduitMR.get_all_productsMR()

      slAV = SiteLiv_AV.objects.all()
      
      slMR = SiteLiv_MR.objects.all()


      if request.method == 'POST':
        formAV = CommandeAVForm(request.POST, instance=request.user.clientav)

        if formAV.is_valid():
            data = CommandeAv()
            data.clientAV = request.user.clientav
            data.produit = formAV.cleaned_data['produit']
            data.quantity = formAV.cleaned_data['quantity']
            data.type_deviseAv = formAV.cleaned_data['type_deviseAv']
            if formAV.cleaned_data['type_deviseAv'] == 'DA':
             data.price = data.produit.prix * formAV.cleaned_data['quantity']
            else :
             data.price = data.produit.prixD * formAV.cleaned_data['quantity'] 
            data.site_Livraison_Aviation = formAV.cleaned_data['site_Livraison_Aviation']
            data.save()

            link = "http://127.0.0.1:8000/admin/"

            msg = '''
                      Clinet : {}
                      Produit : {}
                      Quantity : {}
                      Prix_total : {}
                      Centre de livraison : {}
         
              '''.format(data.clientAV, data.produit, data.quantity, data.price, data.site_Livraison_Aviation)

            send_mail(
                      subject="Nouvelle Commande",
                      message=f"{msg} \n Une nouvelle commande a été établie : {link}",
                      from_email="your@email.com",
                      recipient_list=[settings.EMAIL_HOST_USER]
                  )

            return redirect(to='mesCmdsAV')
           
      else:
        formAV = CommandeAVForm(instance=request.user.clientav)



      
      if request.method == 'POST':
        formMR = CommandeMRForm(request.POST, instance=request.user.clientav)

        if formMR.is_valid():
            data = CommandeMr()
            data.client = request.user.clientav
            data.produitmr = formMR.cleaned_data['produitmr']
            data.quantitymr = formMR.cleaned_data['quantitymr']
            data.type_deviseMr = formMR.cleaned_data['type_deviseMr']
            if formMR.cleaned_data['type_deviseMr'] == 'DA':
             data.pricemr = data.produitmr.prix_mr * formMR.cleaned_data['quantitymr']
            else:
             data.pricemr = data.produitmr.prix_mrD * formMR.cleaned_data['quantitymr'] 
            data.site_Livraison_Marine = formMR.cleaned_data['site_Livraison_Marine']
            data.save()

            link = "http://127.0.0.1:8000/admin/"

            msg = '''
                      Clinet : {}
                      Produit : {}
                      Quantity : {}
                      Prix_total : {}
                      Centre de livraison : {}
         
              '''.format(data.client, data.produitmr, data.quantitymr, data.pricemr, data.site_Livraison_Marine)

            send_mail(
                      subject="Nouvelle Commande",
                      message=f"{msg} \n Une nouvelle commande a été établie : {link}",
                      from_email="your@email.com",
                      recipient_list=[settings.EMAIL_HOST_USER]
                  )

            return redirect(to='mesCmdsAV')
           
      else:
        formMR = CommandeMRForm(instance=request.user.clientav)


      context = {'formAV':formAV, 'formMR': formMR, 'prdAV':prdAV, 'prdMR':prdMR, 'slMR':  slMR, 'slAV':  slAV }

      return render(request, 'User_AVM/etablirCommandeAV.html',context)





################################################  Modifier Commande ########################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def update_cmd(request,pk):

      prdMR = ProduitMR.get_all_productsMR()
      
      slMR = SiteLiv_MR.objects.all()

  
      cmd_MR = CommandeMr.objects.get(id=pk) 
      formMR = CommandeMRForm(instance=cmd_MR)

      if request.method == 'POST':
          formMR = CommandeMRForm(request.POST, instance=cmd_MR)
          
          if formMR.is_valid():
            if cmd_MR.type_deviseMr == 'DA':
             pr_P = cmd_MR.produitmr.prix_mr
            elif cmd_MR.type_deviseMr == '$':
             pr_P = cmd_MR.produitmr.prix_mrD
            cnt = cmd_MR.quantitymr
            cmd_MR.pricemr = pr_P * cnt
            cmd_MR.type_deviseMr = formMR.cleaned_data['type_deviseMr']
            formMR.save()
            return redirect(to='mesCmdsAV')


          
      context = {'formMR': formMR, 'cmd_MR': cmd_MR, 'prdMR':prdMR, 'slMR':  slMR, 'slMR':  slMR}

      return render(request, 'User_AVM/update_cmd.html', context)





##################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def update_cmdav(request,pk):
          

      
      prdAV = ProduitAV.get_all_productsAV()
      
      slAV = SiteLiv_AV.objects.all()

  
      cmd_AV = CommandeAv.objects.get(id=pk) 
      formAV = CommandeAVForm(instance=cmd_AV)

      if request.method == 'POST':
          formAV = CommandeAVForm(request.POST, instance=cmd_AV)
          
          if formAV.is_valid():
            if cmd_AV.type_deviseAv == 'DA':
             pr_Pav = cmd_AV.produit.prix
            elif cmd_AV.type_deviseAv == '$':
             pr_Pav = cmd_AV.produit.prixD
            cnt_av = cmd_AV.quantity
            cmd_AV.price = pr_Pav * cnt_av
            formAV.save()
            return redirect(to='mesCmdsAV')


          
      context = {'formAV':formAV, 'cmd_AV': cmd_AV ,'prdAV':prdAV, 'slAV':  slAV }

      return render(request, 'User_AVM/update_cmdav.html', context)






################################################  Supprimer Commande  ########################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def delete_cmd(request,pk):

      cmd_MR = CommandeMr.objects.get(id=pk) 

      if request.method == 'POST':  
         cmd_MR.delete()

         return redirect(to='mesCmdsAV')

      
      context={'cmd_MR': cmd_MR}

      return render(request, 'User_AVM/delete_cmd.html', context)


##################################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def delete_cmdav(request,pk):


      cmd_AV = CommandeAv.objects.get(id=pk) 

      if request.method == 'POST':  
         cmd_AV.delete()

         return redirect(to='mesCmdsAV')
      

      context={'cmd_AV': cmd_AV}

      return render(request, 'User_AVM/delete_cmdav.html', context)
      
      

   






################################################  Payement Aviation  ########################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def payementAV(request,pk):
      cmdAV = CommandeAv.objects.get(id=pk)

      context = {'cmdAV':cmdAV}
      return render(request, 'User_AVM/payementAV.html', context)




@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def payement_CompletedAV(request):
     body = json.loads(request.body)
     cmd_av = CommandeAv.objects.get(id = body['cmd_id'])


     cmd_av.etat_payementav = True
     cmd_av.save()

     
     p = cmd_av.produit.nomP
     q = cmd_av.quantity
     pr = cmd_av.price
     cl = cmd_av.site_Livraison_Aviation.Nom_SiteAV

     link = "http://127.0.0.1:8000/User_Aviation/mesCmdsAV/"

     msg = '''
         
         Produit : {}
         Quantity : {}
         Prix_total : {}
         Centre de livraison : {}
         
         '''.format(p, q, pr, cl)

     send_mail(
                      subject="Paiment Commande",
                      message=f"{msg} \n Votre paiement effectué avec succès .Merci pour votre confiance, Veuillez attendre que une date de livraison soit fixée: {link}",
                      from_email="your@email.com",
                      recipient_list=[request.user.email]
                  )
     
     linkAd = "http://127.0.0.1:8000/admin/"
     
     msgAd = '''
         
         Client : {}
         Produit : {}
         Quantity : {}
         Prix_total : {}
         Centre de livraison : {}
         
         '''.format(request.user.username,p, q, pr, cl)

     send_mail(
                      subject="Paiment Commande",
                      message=f"{msgAd} \n Paiement effectué avec succès, Veuillez fixée une date de livraison au clinet: {linkAd}",
                      from_email="your@email.com",
                      recipient_list=[settings.EMAIL_HOST_USER]
                  )

     return JsonResponse('Payement Completed')







########################################  Payement Marine  ###############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def payementMR(request,pk):
      cmdMR = CommandeMr.objects.get(id=pk)

      context = {'cmdMR':cmdMR}
      return render(request, 'User_AVM/payementMR.html', context)


@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def payement_CompletedMR(request):
     body = json.loads(request.body)
     cmd_mr = CommandeMr.objects.get(id = body['cmd_id'])


     cmd_mr.etat_payementmr = True
     cmd_mr.save()

     p = cmd_mr.produitmr.nomP_mr
     q = cmd_mr.quantitymr
     pr = cmd_mr.pricemr
     cl = cmd_mr.site_Livraison_Marine.Nom_SiteMR

     link = "http://127.0.0.1:8000/User_Aviation/mesCmdsAV/"

     msg = '''
         
         Produit : {}
         Quantity : {}
         Prix_total : {}
         Centre de livraison : {}
         
         '''.format(p, q, pr, cl)

     send_mail(
                      subject="Paiment Commande",
                      message=f"{msg} \n Votre paiement effectué avec succès .Merci pour votre confiance, Veuillez attendre que une date de livraison soit fixée: {link}",
                      from_email="your@email.com",
                      recipient_list=[request.user.email]
                  )

      
     linkAd = "http://127.0.0.1:8000/admin/"

     msgAd = '''
         
         Client : {}
         Produit : {}
         Quantity : {}
         Prix_total : {}
         Centre de livraison : {}
         
         '''.format(request.user.username,p, q, pr, cl)

     send_mail(
                      subject="Paiment Commande",
                      message=f"{msgAd} \n Paiement effectué avec succès, Veuillez fixée une date de livraison au clinet: {linkAd}",
                      from_email="your@email.com",
                      recipient_list=[settings.EMAIL_HOST_USER]
                  )
          
     return JsonResponse('Payement Completed', safe=False)






############################################### Consulter Cmd's ########################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def mesCmdsAV(request):

      cmd_AV = request.user.clientav.commandeav_set.all().order_by('-id')
      nbrCmd_AV = request.user.clientav.commandeav_set.count() 

      paginator = Paginator(cmd_AV, 6)
      page_num = request.GET.get('page')
      page_objAV = paginator.get_page(page_num)


      cmd_MR = request.user.clientav.commandemr_set.all().order_by('-id')
      nbrCmd_MR = request.user.clientav.commandemr_set.count() 

      paginator_mr = Paginator(cmd_MR, 6)
      page_num_mr = request.GET.get('page')
      page_objMR = paginator_mr.get_page(page_num_mr)


      date_aujourdhui = date.today()


      context = {'page_objAV': page_objAV, 'nbrCmd_AV': nbrCmd_AV, 'page_objMR': page_objMR, 'nbrCmd_MR': nbrCmd_MR, 'date_aujourdhui': date_aujourdhui}

      return render(request, 'User_AVM/mesCmdsAV.html', context)




########################################### Bon de commande Aviation ############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def bon_cmdAV(request,pk):
    cmd_AV = CommandeAv.objects.get(id=pk)
    context = {'cmd_AV': cmd_AV}
    return render(request, 'User_AVM/bon_cmdAV.html', context)


def render_pdf_view(request):
    template_path = 'User_AVM/rf.html'
    context = {}

    # Create a Django response object, and specify content_type as pdf

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bon_commande.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


########################################### Bon de commande Marine ############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def bon_cmdMR(request,pk):
    cmd_MR = CommandeMr.objects.get(id=pk)
    context = {'cmd_MR': cmd_MR}
    return render(request, 'User_AVM/bon_cmdMR.html', context)


def render_pdf_view(request):
    template_path = 'User_AVM/bon_cmdMR.html'
    context = {}

    # Create a Django response object, and specify content_type as pdf

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="bon_commande.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


########################################### Réclamer ############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def réclamation(request):
  
       #  message = '''
        #   Réclamation a la part de {} ,Email: {}

         #  Sujet: {}

          # Contenu: {} 
         
         #'''.format(data['nom'], data['email'], data['sujet'], data['message'])
      n = True
   

      if request.method == 'POST':
        nom = request.user.username
        email = request.user.email
        sujet = request.POST['sujet']
        message = request.POST['message']

        if nom == "" or email == "" or sujet == "" or message == "":
          n = False
          messages.error(request, 'Veuiller Remplir tous les champs !')
        else: 
         
         msg = '''
         
         Réclamation de la part de : {} , email : {}

         Contenu : {}
         
         '''.format(nom, email, message)

         Rec = Reclamation.objects.create(clientRc = nom, emailCl = email, sujet = sujet, message = message)
         Rec.save()

         send_mail(
            sujet,
            msg,
            '',
            [settings.EMAIL_HOST_USER],
        )

        messages.success(request, 'Votre Réclamation a été envoyé, et en cours de traitement. Vous recevrez une réponse dans les plus brefs délais')

      return render(request, 'User_AVM/réclamation.html', {'n':n })







######################################### Update Password ##############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def modifier_mdps(request):

      if request.method == 'POST':
            password_form = PasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                password_form.save()
                messages.success(request, 'Votre Mot de passe a été modifier')
                
      else:
          password_form = PasswordChangeForm(request.user)

      context = {'password_form': password_form}

      return render(request, 'User_AVM/modifier_mdps.html', context)








######################################## Consulter les Sites de livraison ###############################################################
@login_required(login_url='loginAV')
@allowedUsersAV(allowedUsers=['clients'])
def sitelivAV(request):
    
      return render(request, 'User_AVM/sitelivAV.html')








########################################## S'authentifier #############################################################
@notLoggedUsers
def loginAV(request):

      if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request , username=username, password=password)
            if user is not None:
             login(request, user)
             return redirect('profile')
            elif  username == "" and password == "":
                messages.info(request, 'Veuiller saisir vos informations !')
            else:
                messages.error(request, 'Username ou Mot de passe incorrecte !')

      return render(request, 'User_AVM/loginAV.html')







############################################# Déconnecter ##########################################################
def userLogout(request):  
    logout(request)
    return redirect('loginAV') 





#@login_required(login_url='loginAV')
#@allowedUsersAV(allowedUsers=['clients'])
#def userProfileAV(request):

#      return render(request, 'User_Aviation/userProfileAV.html')



    
