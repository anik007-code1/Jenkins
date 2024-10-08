from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import FileResponse
from home.models import PDFDocument, Category


# View to display PDFs by Category
def books_by_category(request, slug):
    category = get_object_or_404(Category, slug=slug)  # Fetch the category based on slug
    pdfs = PDFDocument.objects.filter(category=category)  # Get PDFs for this category
    return render(request, 'books.html', {'category': category, 'pdfs': pdfs})


# View to show details of a specific category
def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    pdfs = PDFDocument.objects.filter(category_name=category)  # Fetch PDFs for the category
    return render(request, 'category_detail.html', {'category': category, 'pdfs': pdfs})


# View to display the PDF file
def PDFDetailView(request, slug):
    pdf = get_object_or_404(PDFDocument, slug=slug)
    return FileResponse(open(pdf.pdf_file.path, 'rb'), content_type='application/pdf')


# View to list all categories
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})


# User Registration View
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already used.")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already used.")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! You can log in now.")
                return redirect('login')
        else:
            messages.info(request, "Passwords do not match.")
            return redirect('register')
    else:
        return render(request, 'register.html')


# User Login View
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect('category_list')
        else:
            messages.error(request, "Invalid credentials. Please try again.")
            return redirect('login')
    else:
        return render(request, 'login.html')


# User Logout View
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('category_list')
