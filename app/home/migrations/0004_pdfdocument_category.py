# Generated by Django 4.2.16 on 2024-10-08 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdocument',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pdfs', to='home.category'),
            preserve_default=False,
        ),
    ]
