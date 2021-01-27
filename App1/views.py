from django.shortcuts import render,redirect
from .models import *
from .form import ContactForm
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def Home(request):
    cate=Category.objects.all()
    images=Image.objects.all().order_by('-added_date')
    
    paginator=Paginator(images,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={'images':images,'cate':cate,'page_obj':page_obj
    }
    return render(request,'App1/Home.html',context)

# def blog(request):
#     posts = Post.objects.all().order_by('-posted_date')
#     paginator = Paginator(posts, 2)

#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {'page_obj': page_obj}
#     return render(request, 'main/blog.html', context)


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
    



    
