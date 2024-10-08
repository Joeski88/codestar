# Generated by Django 4.2.16 on 2024-09-26 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='exerpt',
            new_name='excerpt',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='update_on',
            new_name='updated_on',
        ),
    ]
