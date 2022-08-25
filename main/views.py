from django.shortcuts import render, redirect
from main.models import *
from main.form import *


def index(request):
    portifo = Portofolio.objects.order_by("-id")[:3]
    model = Message()
    form = MessageForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)

    ctx = {
        "form": form,
        "portifo": portifo
    }
    return render(request, "main/index.html", ctx)
