from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.views.generic import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse

# Create your views here.

from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.template.response import TemplateResponse
from django.views.generic.edit import CreateView
from .models import Profile, Restaurant, Noticia, Esdeveniment, FotoRestaurant, ComentariRestaurant, ValoracioRestaurant, SuggerimentRestaurant
import logging
log = logging.getLogger(__name__)


class ProfileForm(forms.ModelForm):
    """Si s'usuari no existeix en validar l'ha de crear i assignar"""
    email=forms.EmailField()
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    datanaixement = forms.CharField()
    def clean(self):
        log.debug('entrant al clean')
        
        cleaned_data=super().clean()
        email=cleaned_data.get('email')
        username=cleaned_data.get('username')
        datanaixement=cleaned_data.get('datanaixement')
        password=cleaned_data.get('password')
        dia=datanaixement.split("-")[0]
        mes=datanaixement.split("-")[1]
        any=datanaixement.split("-")[2]
        datanaixement = any + "-" + mes + "-" + dia
        cleaned_data['datanaixement']=datanaixement
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("L'email ja existeix")
        else:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("El nom d'usuari ja existeix")
            else:
                u=User()
                #u.username = email.split("@",1)[0]  # Agafa abans del simbol @
                u.username = username
                u.set_password(cleaned_data.get('password'))
                
                u.email = email
                u.save()
        
        return cleaned_data

    class Meta:
        model = Profile
        exclude = ['user']

class RestaurantForm(forms.ModelForm):
    def clean(self):
        cleaned_data=super().clean()
        return cleaned_data

    class Meta:
        model = Restaurant
        exclude = ['profile']

class ProfileUpdateForm(forms.ModelForm):

    datanaixement = forms.CharField()
    username = forms.CharField()

    def clean(self):
        cleaned_data=super().clean()
        datanaixement=cleaned_data.get('datanaixement')
        username=cleaned_data.get('username')
        dia=datanaixement.split("-")[0]
        mes=datanaixement.split("-")[1]
        any=datanaixement.split("-")[2]
        datanaixement = any + "-" + mes + "-" + dia
        cleaned_data['datanaixement']=datanaixement

        return cleaned_data

    class Meta:
        model = Profile
        exclude = ['password', 'user']

class RestaurantComentariForm(forms.ModelForm):
    profile=forms.CharField()
    def clean(self):
        log.debug('entrant al clean')
        
        cleaned_data=super().clean()
        restaurant=cleaned_data.get('restaurant')
        try:
            profile=Profile.objects.get(id=cleaned_data.get('profile'))
            cleaned_data['profile']=profile
        except Profile.DoesNotExist:
            raise forms.ValidationError("L'usuari no existeix")

        if not Restaurant.objects.filter(pk=restaurant.id).exists():
            raise forms.ValidationError("El restaurant no existeix")

        return cleaned_data

    class Meta:
        model = ComentariRestaurant
        fields = "__all__"

class RestaurantValoracioForm(forms.ModelForm):
    profile=forms.CharField()
    def clean(self):
        log.debug('entrant al clean')
        cleaned_data=super().clean()
        restaurant=cleaned_data.get('restaurant')
        try:
            profile=Profile.objects.get(id=cleaned_data.get('profile'))
            cleaned_data['profile']=profile
        except Profile.DoesNotExist:
            raise forms.ValidationError("L'usuari no existeix")

        if not Restaurant.objects.filter(pk=restaurant.id).exists():
            raise forms.ValidationError("El restaurant no existeix")

        return cleaned_data

    class Meta:
        model = ValoracioRestaurant
        fields = "__all__"

class RestaurantSuggerimentActualitzaForm(forms.ModelForm):
    
    def clean(self):
        log.debug('entrant al clean')
        cleaned_data=super().clean()
        #import pdb; pdb.set_trace()
        #cleaned_data['restaurant'] = Restaurant.objects.get(id=cleaned_data.get('id'))

        return cleaned_data

    class Meta:
        model = SuggerimentRestaurant
        exclude = ['profile', 'restaurant']

@method_decorator(csrf_exempt, name='dispatch')
class ProfileCreate(CreateView):
    def post(self, request):
        log.debug('entrant al post de profile')
        data = dict()
        form = ProfileForm(request.POST)
        """
        1. Comprovar que l'usuari no existeix
        1.1 Si no existeix el cream i en el guardam per assignar-lo al model
        1.2 Si existeix donam error
        """
        # AUTOCOMMIT FALSE! Millor fer-ho tot manual a l'hora de guardar la variable "user"
        if form.is_valid():
            
            user = User.objects.get(email=form.cleaned_data.get('email'))
            
            obj, created = Profile.objects.update_or_create(user=user, 
                defaults={'nomillinatges': form.cleaned_data.get('nomillinatges'), 
                'datanaixement': form.cleaned_data.get('datanaixement'), 
                'direccio': form.cleaned_data.get('direccio'),
                'telefon': form.cleaned_data.get('telefon'),
                'fotoperfil': form.cleaned_data.get('fotoperfil')}
            )
        else:
            user = User.objects.get(email=form.cleaned_data.get('email'))
            # Si l'usuari està creat i el perfil no, s'ha de borrar l'usuari (excepte l'administrador)
            if not user.is_superuser:
                if not hasattr(user, 'profile'):
                    user.delete()
            data['error'] = "Formulari invàlid!"
            data['errors'] = form.errors
            log.error('Error en el registre {}'.format(form.errors))
        return JsonResponse(data)

class ProfileUpdate(UpdateView):

    def post(self, request, pk):
        log.debug('entrant al post de profile')
        data = dict()
        form = ProfileUpdateForm(request.POST, request.FILES)
        username_id = self.request.user.id
        profile = Profile.objects.get(user_id=username_id)

        # AUTOCOMMIT FALSE!
        if form.is_valid():

            """ Comprovar que l'usuari no existeix quan el canvies de nom """

            username = form.cleaned_data.get('username')

            if User.objects.exclude(id=username_id).filter(username=username).exists():
                data['error'] = 'Error: Usuari duplicat: {}'.format(username)
                data['errors'] = form.errors
                log.error('Error: Usuari duplicat: {}'.format(username))
            else:
                profile.nomillinatges = form.cleaned_data.get('nomillinatges')
                profile.datanaixement = datetime.strptime(form.cleaned_data.get('datanaixement'), '%Y-%m-%d').date()
                profile.direccio = form.cleaned_data.get('direccio')
                profile.telefon = form.cleaned_data.get('telefon')
                profile.fotoperfil = form.cleaned_data.get('fotoperfil')
                #profileUpdate = form.save(commit=False)
                profile.save()
                data['correcte'] = "Perfil actualitzat satisfactòriament!"
        else:
            data['error'] = "Formulari invàlid!"
            data['errors'] = form.errors
            log.error('Error en actualitzar el perfil {}'.format(form.errors))
        request.session['data'] = data
        return redirect('/perfil/' + str(profile.id) + "/")

@method_decorator(csrf_exempt, name='dispatch')
class RestaurantCreate(CreateView):
    def post(self, request):
        log.debug("Entrant al post de restaurant")
        
        username_id = self.request.user.id
        profile = Profile.objects.get(user_id=username_id)

        data = dict()
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.profile = profile
            restaurant.save()
        else:
            data['errors'] = form.errors
            log.error('Error en la creació del restaurant {}'.format(form.errors))
        return redirect('/restaurants/')


@method_decorator(csrf_exempt, name='dispatch')
class RestaurantComentariCreate(CreateView):
    def post(self, request):
        log.debug('entrant al post de comentari restaurant')
        
        data = dict()
        form = RestaurantComentariForm(request.POST)
        """
        1. Comprovar que l'id del perfil i l'id del restaurant hi són
        """
        if form.is_valid():
            form.save()
        else:
            data['errors'] = form.errors
            log.error('Error en la creació del comentari {}'.format(form.errors))
        return JsonResponse(data)


@method_decorator(csrf_exempt, name='dispatch')
class RestaurantValoracioCreate(CreateView):
    def post(self, request):
        log.debug('entrant al post de comentari restaurant')
        
        data = dict()
        form = RestaurantValoracioForm(request.POST)
        """
        1. Comprovar que l'id del perfil i l'id del restaurant hi són
        2. Si resulta que l'usuari ja té una valoració d'aquest restaurant, no en crees una nova, només l'actualitzes
        """
        if form.is_valid():
            restaurant = form.cleaned_data.get('restaurant')
            profile = form.cleaned_data.get('profile')
            obj, created = ValoracioRestaurant.objects.update_or_create(restaurant=restaurant, 
                profile=profile,
                defaults={'valoracio': form.cleaned_data.get('valoracio')})
        else:
            data['errors'] = form.errors
            log.error('Error en enviar la valoració {}'.format(form.errors))
        return JsonResponse(data)


class ProfileDetail(DetailView):

    model = Profile
    template_name="html/perfil.html"

    # Borra la sessió, ja que només és necessària per actualitzar el perfil
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if('data' in self.request.session):
            context['data'] = self.request.session['data']
            del self.request.session['data']
            
        return context

    def get_object(self, queryset=None):
        user = self.request.user
        # Agafa pk de la URL
        pk = self.kwargs.get(self.pk_url_kwarg)
        profile = Profile.objects.get(pk=pk)

        # Si el perfil de l'usuari no correspon a l'usuari, fes una fallida (500)
        if profile.user != user:
           return HttpResponse(status=500)
        else:
            return profile

class RestaurantList(ListView):

    model = Restaurant
    template_name="html/restaurants.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        if 'id' in self.request.GET:
            param=self.request.GET['id']

            # Si tens un ID, t'agafa tots els que coincideixen amb aquest ID (tan sols n'hi haurà un perquè és PK)

            restaurant_actual=self.model.objects.get(id=param)
            context['restaurant']=restaurant_actual

            # Agafa la foto del restaurant (si en té)

            if FotoRestaurant.objects.filter(restaurant_id=param).exists():
                foto_restaurant=FotoRestaurant.objects.filter(restaurant_id=param).first()
                context['foto_restaurant']=foto_restaurant

            # Agafa els comentaris del restaurant (si en té)

            if ComentariRestaurant.objects.filter(restaurant_id=param).exists():
                
                comentaris_restaurant=ComentariRestaurant.objects.filter(restaurant_id=param).all().order_by("-data")
                context['comentaris_restaurant']=comentaris_restaurant

            # Agafa la valoració que ha fet l'usuari (ha d'haver iniciat sessió)

            if self.request.user.is_authenticated:
                profile = Profile.objects.get(user=self.request.user)
                try:
                    v = ValoracioRestaurant.objects.get(restaurant_id=param, profile=profile).valoracio
                except ValoracioRestaurant.DoesNotExist:
                    v = 0

                context['stars']=v
        
        if 'cerca' in self.request.GET:
            param=self.request.GET['cerca']
            #import pdb; pdb.set_trace()
            if param:
                # Selecciona els restaurants que són visibles i contenen el paràmetre de cerca (al seu nom)
                postresult = Restaurant.objects.filter(nom__contains=param).filter(visible=True)[:10]
                context['cerca'] = postresult
                context['cerca_param'] = param
            else:
                postresult = None
                context['cerca'] = postresult
                context['cerca_param'] = param
                
        return context

class RestaurantSuggerimentList(ListView):

    model = Restaurant
    template_name="html/actu_restaurant.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        if 'id' in self.request.GET:
            param=self.request.GET['id']

            # Si tens un ID, t'agafa tots els que coincideixen amb aquest ID (tan sols n'hi haurà un perquè és PK)

            restaurant_actual=self.model.objects.get(id=param)
            context['restaurant']=restaurant_actual

            # Agafa la foto del restaurant (si en té)

            if FotoRestaurant.objects.filter(restaurant_id=param).exists():
                foto_restaurant=FotoRestaurant.objects.filter(restaurant_id=param).first()
                context['foto_restaurant']=foto_restaurant

            # Agafa els comentaris del restaurant (si en té)

            if ComentariRestaurant.objects.filter(restaurant_id=param).exists():
                
                comentaris_restaurant=ComentariRestaurant.objects.filter(restaurant_id=param).all().order_by("-data")
                context['comentaris_restaurant']=comentaris_restaurant

            # Agafa la valoració que ha fet l'usuari (ha d'haver iniciat sessió)

            if self.request.user.is_authenticated:
                profile = Profile.objects.get(user=self.request.user)
                try:
                    v = ValoracioRestaurant.objects.get(restaurant_id=param, profile=profile).valoracio
                except ValoracioRestaurant.DoesNotExist:
                    v = 0

                context['stars']=v

        if 'cerca' in self.request.GET:
            param=self.request.GET['cerca']
            import pdb; pdb.set_trace()
            if param:
                # Selecciona els restaurants que són visibles i contenen el paràmetre de cerca (al seu nom)
                postresult = Restaurant.objects.filter(nom__contains=param).filter(visible=True)[:10]
                context['cerca'] = postresult
                context['cerca_param'] = param
            else:
                postresult = None
                context['cerca'] = postresult
                context['cerca_param'] = param
                
        return context

class RestaurantSuggerimentActualitza(ListView):

    model = SuggerimentRestaurant
    template_name="html/actu_restaurant.html"

    def post(self, request):
        log.debug("Entrant al post de restaurant")
        #import pdb; pdb.set_trace()
        data = dict()

        username_id = self.request.user.id
        profile = Profile.objects.get(user_id=username_id)
        restaurant = Restaurant.objects.get(id=request.GET['id'])

        form = RestaurantSuggerimentActualitzaForm(request.POST)
        if form.is_valid():
            suggeriment = form.save(commit=False)
            suggeriment.profile = profile
            suggeriment.restaurant = restaurant
            suggeriment.save()
        else:
            data['errors'] = form.errors
            log.error('Error en la creació del restaurant {}'.format(form.errors))
        return redirect('/restaurants/')

class RestaurantMapaList(ListView):
    def get(self, request):
        restaurants = list(Restaurant.objects.all().values())
        data = dict()
        data['restaurants'] = restaurants
        return JsonResponse(data)

class NoticiaList(ListView):

    model = Noticia
    template_name="html/noticies.html"

    ordering = ['-data']

class EsdevenimentList(ListView):

    model = Esdeveniment
    template_name="html/esdeveniments.html"

    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        if 'id' in self.request.GET:
            param=self.request.GET['id']
            # Si tens un ID, t'agafa tots els que coincideixen amb aquest ID (tan sols n'hi haurà un perquè és PK)
            esdeveniment_actual=self.model.objects.get(id=param)
            context['esdeveniment']=esdeveniment_actual
        return context