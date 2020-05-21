from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.core.mail import send_mail
from .models import Blog


def home(request):
    return render(request, 'home.html', {})


def appointment(request):
    return render(request, 'appointment.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message_name']
        message_email = request.POST['message_email']
        message = request.POST['message']

        send_mail(
            'messge from ' + message_name,
            message,
            message_email,
            ['exactmusty1994@gmail.com', 'jazeera@gmail.com'],
        )
        return render(request, 'contact.html', {'message_name': message_name})
    else:
        return render(request, 'contact.html', {})


def doctor(request):
    return render(request, 'doctor.html', {})


def blog(request):
    blog_post = Blog.objects.all()
    paginator = Paginator(blog_post, 1)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset =paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)
    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var
    }

    return render(request, 'blog.html', context)

 
def lab(request):
    return render(request, 'lab.html', {})
