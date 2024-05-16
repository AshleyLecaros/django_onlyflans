from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


from .models import ContactForm, Flan
from .forms import ContactFormForm, RegistroClienteForm

# Create your views here.

def index(request):
    flanes_pub = Flan.objects.filter(is_private=False)
    return render(request, 'index.html', {"flanes_pub": flanes_pub})

def about(request):
    return render(request, 'about.html', {})

@login_required
def welcome(request):
    flanes_priv = Flan.objects.filter(is_private=True)
    nombre_usuario = request.user.username
    return render(request, 'welcome.html', {'nombre_usuario': nombre_usuario, 'flanes_priv': flanes_priv})


def contact(request):
    if request.method == "POST":
        form = ContactFormForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect("/gracias")
    else:
        form = ContactFormForm()
    return render(request, "contact.html", {"form": form})

def gracias(request):
    return render(request, 'gracias.html', {})

def registrar_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome') 
    else:
        form = RegistroClienteForm()
    return render(request, 'registro_cliente.html', {'form': form})


