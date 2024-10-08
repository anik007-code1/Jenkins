from django import forms
from .models import Category, PDFDocument

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class PDFDocumentForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['title', 'pdf_file']
