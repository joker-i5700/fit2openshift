# Generated by Django 2.1.2 on 2019-04-15 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openshift_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenshiftCluster',
            fields=[
                ('abstractcluster_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='openshift_base.AbstractCluster')),
            ],
            bases=('openshift_base.abstractcluster',),
        ),
    ]
