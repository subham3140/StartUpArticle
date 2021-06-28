# Generated by Django 3.2 on 2021-06-28 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articleapp', '0019_auto_20210628_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewcontent',
            name='content_type',
            field=models.CharField(choices=[('question', 'Question'), ('answers', 'Answers'), ('inspiration', 'Inspiration'), ('success_key', 'Success Key'), ('story', 'story'), ('idea', 'Idea'), ('achievement', 'Achievement'), ('influencer', 'Influencer'), ('contact', 'Contact'), ('goal', 'Goal')], default='question', max_length=200),
        ),
    ]
