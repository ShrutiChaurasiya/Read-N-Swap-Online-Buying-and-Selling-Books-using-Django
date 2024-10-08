# Generated by Django 4.2.11 on 2024-03-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0006_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookname', models.TextField()),
                ('author_name', models.TextField()),
                ('book_desc', models.TextField()),
                ('book_price', models.CharField(max_length=10)),
                ('bookimage', models.ImageField(default='', upload_to='pimage/')),
            ],
        ),
    ]
