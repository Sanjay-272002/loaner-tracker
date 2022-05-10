# Generated by Django 4.0.4 on 2022-05-09 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profilescreen', '0002_book_delete_user_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountnumber', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('phonenumber', models.CharField(max_length=200)),
                ('aadharcard', models.FileField(upload_to='datas/pdfs')),
                ('pancard', models.FileField(upload_to='datas/pdfs')),
                ('salaryslips', models.FileField(upload_to='datas/pdfs')),
                ('photo', models.FileField(upload_to='datas/pdfs')),
            ],
        ),
        migrations.DeleteModel(
            name='Book',
        ),
    ]