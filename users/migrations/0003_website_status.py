# Generated by Django 4.0.2 on 2022-02-09 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='status',
            field=models.CharField(choices=[('R', 'Reviewd'), ('N', 'Not Reviewed'), ('E', 'Error'), ('A', 'Accepted')], default='R', max_length=1),
            preserve_default=False,
        ),
    ]
