from django.shortcuts import render,redirect
from .models import *
from .form import ContactForm
from django.contrib import messages

# Create your views here.
def Home(request):
    cate=Category.objects.all()
    images=Image.objects.all()
    context={'images':images,'cate':cate,
    }
    return render(request,'App1/Home.html',context)

def category(request,cid):
    cate=Category.objects.all()

    ImageCategory=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=ImageCategory)
    context={'images':images,'cate':cate,
    }
    return render(request,'App1/Home.html',context)


def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)

        name = instance.name
        email = instance.email
        message = instance.message

       

        form.save()

        messages.success(request, 'Thanks For Contacting With Us:)!')

        return redirect('contact')

    context = {'form': form}
    return render(request, 'App1/contact.html', context)
    



    
