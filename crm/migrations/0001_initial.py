# Generated by Django 4.1.7 on 2023-03-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='female', max_length=200)),
                ('salary', models.PositiveIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images')),
                ('address', models.CharField(max_length=200)),
            ],
        ),
    ]
