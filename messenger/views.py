from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from .models import Thread, Message

@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread
    
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        
        # Marcar los mensajes como leídos solo si el remitente no es el usuario actual
        for message in obj.messages.filter(user__id=obj.users.exclude(id=self.request.user.id).first().id):
            if not message.is_read:
                message.is_read = True
                message.save()
        
        return obj

def add_message(request, pk):
    json_response = {'created': False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) == 1:
                json_response['first'] = True

            # Envía un mensaje al grupo del hilo utilizando el canal
            channel_layer = get_channel_layer()
            thread_group_name = f"thread_{pk}"
            async_to_sync(channel_layer.group_send)(
                thread_group_name,
                {
                    "type": "chat_message",
                    "message": {
                        "type": "new_message",
                        "content": content,
                        "username": request.user.username
                    },
                },
            )

    else:
        raise Http404("User is not authenticated")

    return JsonResponse(json_response)

@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))