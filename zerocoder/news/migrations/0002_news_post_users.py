# Generated manually

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news_post',
            name='users',
            field=models.CharField(
                default='Неизвестный пользователь',
                max_length=50,
                verbose_name='Имя пользователя оппобупликовавшего новость'
            ),
        ),
    ]
