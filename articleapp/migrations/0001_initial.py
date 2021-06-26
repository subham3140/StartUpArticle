# Generated by Django 3.2 on 2021-06-25 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('content', models.TextField()),
                ('content_type', models.CharField(choices=[('question', 'Question'), ('advise', 'Advise'), ('achievement', 'Achievement'), ('success_key', 'Success Key'), ('contact', 'Contact'), ('goal', 'Goal'), ('other', 'Other')], max_length=200)),
                ('image', models.ImageField(null=True, upload_to='interview Image')),
                ('video', models.FileField(null=True, upload_to='video/%y')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.CharField(max_length=500)),
                ('profile', models.ImageField(null=True, upload_to='profile')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articleapp.interview')),
            ],
        ),
    ]