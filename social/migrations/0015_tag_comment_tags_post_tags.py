# Generated by Django 4.0.4 on 2022-05-20 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_alter_post_options_post_shared_body_post_shared_on_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='tags',
            field=models.ManyToManyField(blank=True, to='social.tag'),
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='social.tag'),
        ),
    ]
