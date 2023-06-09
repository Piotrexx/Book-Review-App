# Generated by Django 4.1.7 on 2023-05-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_book_contributor_review_bookcontributor_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_upload', models.ImageField(upload_to='images/')),
                ('file_upload', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(help_text='tekst recenzji', max_length=100),
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(help_text='ocena użytkownika od 0 do 10'),
        ),
    ]
