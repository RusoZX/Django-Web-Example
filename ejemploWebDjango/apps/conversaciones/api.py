import json

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from apps.notification.utilities import create_notification

from .models import Mensaje

@login_required
def api_add_mensaje(request):
    data = json.loads(request.body)
    contenido = data['contenido']
    id_conversacion= data['id_conversacion']

    mensaje = Mensaje.objects.create(id_conversacion= id_conversacion, created_by=request.user)

    to_user = None

    for user in mensaje.conversacion.users.all():
        if user != request.user:
            create_notification(request, user, 'mensaje')


    return JsonResponse({'success': True})