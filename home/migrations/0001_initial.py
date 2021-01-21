# Generated by Django 3.1.5 on 2021-01-18 19:37

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('image', models.FileField(blank=True, null=True, upload_to='', verbose_name='yazar Fotoğraf Ekleyin')),
                ('filter', models.CharField(max_length=50, verbose_name='filtre')),
                ('date_birth', models.CharField(max_length=100, verbose_name='Doğum Tarihi')),
                ('date_death', models.CharField(max_length=100, verbose_name='Ölüm Tarihi')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='İnfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Quotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('content', models.CharField(max_length=100, verbose_name='Alıntı')),
                ('conten_quotations', ckeditor.fields.RichTextField(verbose_name='Alıntılar')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.author')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
