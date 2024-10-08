# Generated by Django 5.0.6 on 2024-07-18 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMainContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, null=True)),
                ('subheader', models.TextField(blank=True, null=True)),
                ('mainBodyContent', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='service_images/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
