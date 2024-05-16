# Generated by Django 4.2.11 on 2024-05-14 20:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0002_contactform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_form_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contraseña', models.CharField(max_length=100)),
            ],
        ),
    ]