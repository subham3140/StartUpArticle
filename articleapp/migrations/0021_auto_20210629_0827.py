# Generated by Django 3.2 on 2021-06-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0020_alter_interviewcontent_content_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewcontent',
            name='media',
        ),
        migrations.AddField(
            model_name='interviewcontent',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='interview_image'),
        ),
        migrations.AddField(
            model_name='interviewcontent',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='video/%y'),
        ),
        migrations.DeleteModel(
            name='MediaArticle',
        ),
    ]
