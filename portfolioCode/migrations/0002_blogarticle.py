# Generated by Django 4.1.4 on 2024-09-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioCode', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blogArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('article', models.TextField()),
            ],
        ),
    ]
