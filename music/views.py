from django.views import generic
from .models import Album
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailsView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre_models', 'album_logo']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre_models', 'album_logo']

class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class=UserForm
    template_name='music/registration_form.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form':form})
    #process from data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            #normalize data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #authenticate
            user = authenticate(username=username,password=password)

            if user is not None :
                if user.is_active:
                    login(request,user)
                    return redirect('music:details')
        return render(request,self.template_name,{'form':form})
