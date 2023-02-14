# Generated by Django 4.1.6 on 2023-02-10 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testmonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='profile', verbose_name='picture')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('text', models.CharField(max_length=255, verbose_name='text')),
            ],
            options={
                'verbose_name': 'Testmonial',
                'verbose_name_plural': 'Testmonials',
            },
        ),
    ]