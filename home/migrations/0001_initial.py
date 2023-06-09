# Generated by Django 3.2.18 on 2023-05-01 06:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(blank=True, max_length=200)),
                ('lastname', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('profile_pic', models.ImageField(default='profiles/img.jpg', upload_to='profiles')),
                ('bio', models.CharField(blank=True, max_length=200)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('following', models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='post_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=200)),
                ('post', models.TextField()),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.ManyToManyField(blank=True, default=0, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('post_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.userprofile')),
                ('user', models.ForeignKey(max_length=200, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='home.post_table')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='home.userprofile')),
            ],
        ),
    ]
