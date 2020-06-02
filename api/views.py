from django.views.generic import View
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your views here.

from django.http import JsonResponse
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.template.response import TemplateResponse
from django.views.generic.edit import CreateView
from .models import Profile, Restaurant, Noticia
import logging
log = logging.getLogger(__name__)


class ProfileForm(forms.ModelForm):
    """Si s'usuari no existeix en validar l'ha de crear i assignar"""
    email=forms.EmailField()
    username=forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    def clean(self):
        log.debug('entrant al clean')
        #import pdb; pdb.set_trace()
        cleaned_data=super().clean()
        email=cleaned_data.get('email')
        username=cleaned_data.get('username')
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
                import pdb; pdb.set_trace()
                u.email = email
                u.save()
        
        return cleaned_data

    class Meta:
        model = Profile
        exclude = ['user']


"""class ProfileList(View):
    def get(self, request):
        profiles = list(Profile.objects.all().values())
        data = dict()
        data['profiles'] = profiles
        return JsonResponse(data)


class ProfileListLast(View):
    def get(self, request):
        profiles = list(Profile.objects.latest().values())
        data = dict()
        data['profiles'] = profiles
        return JsonResponse(data)


class ProfileDetail(View):
    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        data = dict()
        data['profile'] = model_to_dict(profile)
        return JsonResponse(data)"""


@method_decorator(csrf_exempt, name='dispatch')
class ProfileCreate(CreateView):
    def post(self, request):
        log.debug('entrant al post de profile')
        data = dict()
        form = ProfileForm(request.POST)
        #no volem gravar directe
        """
        1. Comprovar que l'usuari no existeix
        1.1 Si no existeix el cream i en el guardam per assignar-lo al model
        1.2 Si existeix donam error
        """
        # AUTOCOMMIT FALSE! Millor fer-ho tot manual a l'hora de guardar la variable "user"
        if form.is_valid():
            profile = form.save(commit=False)
            user = User.objects.get(email=form.cleaned_data.get('email'))
            profile.user = user
            profile.save()
            #data['profile'] = model_to_dict(profile)
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


"""class ProfileUpdate(View):
    def post(self, request, pk):
        data = dict()
        profile = Profile.objects.get(pk=pk)
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save()
            data['profile'] = model_to_dict(profile)
        else:
            data['error'] = "form not valid!"
        return JsonResponse(data)


class ProfileDelete(View):
    def post(self, request, pk):
        data = dict()
        profile = Profile.objects.get(pk=pk)
        if profile:
            profile.delete()
            data['message'] = "Profile deleted!"
        else:
            data['message'] = "Error!"
        return JsonResponse(data)"""

class RestaurantList(ListView):

    model = Restaurant
    template_name="html/restaurants.html"

    def get_context_data(self, **kwargs):
        #import pdb; pdb.set_trace()
        context = super().get_context_data(**kwargs)
        return context


class RestaurantMapaList(ListView):
    def get(self, request):
        restaurants = list(Restaurant.objects.all().values())
        data = dict()
        data['restaurants'] = restaurants
        return JsonResponse(data)

class NoticiaList(ListView):

    model = Noticia
    template_name="html/noticies.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context