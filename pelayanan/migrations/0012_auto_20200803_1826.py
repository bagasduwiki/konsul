# Generated by Django 3.0.7 on 2020-08-03 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pelayanan', '0011_auto_20200803_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='admin',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='client',
        ),
        migrations.AddField(
            model_name='chat',
            name='pengaduan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pelayanan.Pengaduans'),
        ),
    ]
