# Generated by Django 3.2 on 2021-05-10 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blog_short_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=40)),
                ('phone', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
