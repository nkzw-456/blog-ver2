# Generated by Django 3.2.7 on 2021-09-22 08:31

import blog2.models
from django.db import migrations, models
import django.db.models.deletion
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug_name', models.CharField(max_length=20)),
                ('slug_eng', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=20)),
                ('tag_eng', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.CharField(default=blog2.models.create_id, editable=False, max_length=22, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('text', markdownx.models.MarkdownxField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog2.category')),
                ('tag', models.ManyToManyField(blank=True, to='blog2.Tags')),
            ],
        ),
    ]