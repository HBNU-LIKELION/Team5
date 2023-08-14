# Generated by Django 4.2.4 on 2023-08-14 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KakaoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kakao_id', models.IntegerField(unique=True, verbose_name='Kakao_id')),
                ('nickname', models.CharField(max_length=128, verbose_name='Sense NickName')),
                ('post_count', models.IntegerField(verbose_name='Post Count')),
            ],
        ),
    ]