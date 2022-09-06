# Generated by Django 4.0.5 on 2022-09-04 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kitaplar', '0003_kuruluslar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Takip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kullanici', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('kuruluslar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kitaplar.kuruluslar')),
            ],
        ),
    ]