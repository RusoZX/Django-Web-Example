from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Notification


# Create your views here.
@login_required
def notifications(request):
    goto = request.GET.get('goto','')
    notification_id = request.Get.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read= True
        notification.save()
        if notification.notification_type == Notification.MENSAJE:
            return redirect('conversacion', user_id=notification.created_by.id)
        else:
            return redirect('userprofile', username=notification.created_by.username)
    
    return render(request, 'notification/notififications.html')
        
