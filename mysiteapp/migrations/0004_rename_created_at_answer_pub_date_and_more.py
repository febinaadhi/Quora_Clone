# Generated by Django 4.1.4 on 2023-07-30 22:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysiteapp', '0003_remove_question_like_count_remove_question_pub_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='created_at',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='created_at',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='view_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]