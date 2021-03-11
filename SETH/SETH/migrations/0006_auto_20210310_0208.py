# Generated by Django 3.1.7 on 2021-03-10 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SETH', '0005_auto_20210310_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auser',
            name='authentication',
        ),
        migrations.RemoveField(
            model_name='buser',
            name='authentication',
        ),
        migrations.RemoveField(
            model_name='cuser',
            name='authentication',
        ),
        migrations.AddField(
            model_name='userauthentication',
            name='auser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SETH.auser'),
        ),
        migrations.AddField(
            model_name='userauthentication',
            name='buser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SETH.buser'),
        ),
        migrations.AddField(
            model_name='userauthentication',
            name='cuser',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SETH.cuser'),
        ),
    ]