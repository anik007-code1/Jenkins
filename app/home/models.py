from django.db import models
from django.utils.text import slugify

class PDFDocument(models.Model):
    title = models.CharField(max_length=255, help_text="Enter the title of the PDF")
    slug = models.SlugField(unique=True, blank=True, null=True)
    pdf_file = models.FileField(upload_to='pdfs/', help_text="Upload the PDF file")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(PDFDocument, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
