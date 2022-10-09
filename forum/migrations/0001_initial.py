# Generated by Django 4.0.6 on 2022-09-29 08:26

import ckeditor.fields
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
            name='Forum',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=400)),
                ('body', ckeditor.fields.RichTextField()),
                ('posted_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_author', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(related_name='forum_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('text', models.TextField(default='')),
                ('commented_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_comment_author', to=settings.AUTH_USER_MODEL)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.forum')),
                ('likes', models.ManyToManyField(related_name='forum_comment_likes', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.comment')),
            ],
        ),
    ]
