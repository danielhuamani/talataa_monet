# Generated by Django 4.1.7 on 2023-03-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_alter_question_options_alter_questionoption_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]