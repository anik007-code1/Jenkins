from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from home.models import PDFDocument
from django.shortcuts import get_object_or_404
from django.http import FileResponse


def PDFDetailView(request, slug):
    pdf = get_object_or_404(PDFDocument, slug=slug)
    return FileResponse(open(pdf.pdf_file.path, 'rb'), content_type='application/pdf')

def home(request):
    pdf = PDFDocument.objects.all()
    return render(request, 'home.html', {'pdfs': pdf})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already Used")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, "Password Not the Same")
            return redirect('register')
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
