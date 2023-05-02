from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Conversacion, Mensaje
from django.contrib.auth.models import User
# Create your views here.

@login_required
def conversaciones(request):
    conversaciones= request.user.conversaciones.all()

    return render(request, 'conversacion/conversacion.html', {'conversaciones': conversaciones})

@login_required
def conversacion(request, user_id):
    conversaciones = Conversacion.objects.filter(user__in=[request.user.id])
    conversaciones = conversaciones.filter(user__in=[user_id])

    if conversaciones.count() == 1:
        conversacion = conversaciones[0]
    else:
        recipiente = User.objects.get(pk=user_id)
        conversacion= Conversacion.objects.create()
        conversacion.users.add(request.user)
        conversacion.users.add(recipiente)
        conversacion.save()

    return render(request, 'conversacion/conversacion.html', {'conversacion':conversacion})
