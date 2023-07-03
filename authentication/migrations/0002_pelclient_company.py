# Generated by Django 3.2.3 on 2023-07-02 08:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelclient',
            name='company',
            field=models.ForeignKey(db_column='client_parent_company', default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='company', to='authentication.clientcompany', to_field='company_name'),
            preserve_default=False,
        ),
    ]
