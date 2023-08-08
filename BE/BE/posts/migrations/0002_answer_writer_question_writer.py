# Generated by Django 4.2.4 on 2023-08-08 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_student'),
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher'),
        ),
        migrations.AddField(
            model_name='question',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.student'),
        ),
    ]