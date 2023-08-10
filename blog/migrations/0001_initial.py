# Generated by Django 4.0.4 on 2023-08-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('description', models.TextField(verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='изображение')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='просмотры')),
            ],
            options={
                'verbose_name': 'блог',
                'verbose_name_plural': 'статьи',
            },
        ),
    ]