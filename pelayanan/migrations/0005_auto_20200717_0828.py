# Generated by Django 3.0.8 on 2020-07-17 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pelayanan', '0004_auto_20200717_0817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pengaduan',
            name='oleh',
        ),
        migrations.RemoveField(
            model_name='pengaduan',
            name='respon',
        ),
        migrations.CreateModel(
            name='Respons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jawab', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('pengaduan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pelayanan.Pengaduan')),
            ],
        ),
    ]
