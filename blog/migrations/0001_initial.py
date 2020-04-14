# Generated by Django 2.2.6 on 2020-04-14 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='请输入博客标题', max_length=50)),
                ('date', models.DateField()),
                ('image', models.ImageField(default='default.png', upload_to='images/')),
                ('text', models.TextField(default='请输入正文', max_length=500)),
            ],
        ),
    ]