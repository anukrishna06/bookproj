# Generated by Django 5.1.1 on 2024-09-26 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookcardapp', '0003_book_delete_card'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=220)),
                ('author', models.CharField(max_length=220)),
                ('image', models.ImageField(null=True, upload_to='image')),
                ('description', models.TextField(null=True)),
            ],
            options={
                'db_table': 'BOOKCARD',
            },
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]
