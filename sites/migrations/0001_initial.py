# Generated by Django 3.1.14 on 2022-07-25 18:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SiteBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('block_type', models.SmallIntegerField(choices=[(1, 'Authorization'), (2, 'Catalog'), (3, 'Contacts')])),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blocks', to='sites.usersite')),
            ],
            options={
                'unique_together': {('block_type', 'site')},
            },
        ),
    ]