from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from datetime import datetime
from .models import Message
from .forms import MessageForm

def message_list(request):
    queryset = Message.objects.filter(is_archived=False)
    date_str = request.GET.get('date')
    if date_str:
        try:
            filter_date = datetime.strptime(date_str, '%Y-%m-%d').date()
            queryset = queryset.filter(created_at__date=filter_date)
        except ValueError:
            pass
    return render(request, 'chat/messages.html', {'messages_list': queryset})

def edit_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваше сообщение было успешно отредактировано.")
            return redirect('message_list')
    else:
        form = MessageForm(instance=message)
    return render(request, 'chat/messages.html', {'form': form, 'edit_mode': True, 'message': message})

def delete_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        message.is_archived = True
        message.save()
        messages.success(request, "Ваше сообщение было успешно удалено.")
        return redirect('message_list')

def restore_message(request, pk):
    message = get_object_or_404(Message, pk=pk)
    if request.method == "POST":
        message.is_archived = False
        message.save()
        messages.success(request, "Сообщение успешно восстановлено.")
        return redirect('message_list')

