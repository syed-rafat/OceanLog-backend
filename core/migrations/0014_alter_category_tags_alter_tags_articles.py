# Generated by Django 4.0.5 on 2022-08-18 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_category_tags_alter_tags_articles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='categories', to='core.tags'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='articles',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='core.article'),
        ),
    ]
