# Generated by Django 4.1.5 on 2023-01-23 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('universitygo', '0002_university_after_alter_university_img1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Создатель',
                'verbose_name_plural': 'Создатели',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='university',
            name='who_is_creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='post_creator', to='universitygo.creator', verbose_name='Создатель поста'),
        ),
    ]