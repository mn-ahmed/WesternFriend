# Generated by Django 2.2.9 on 2020-01-29 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0014_magazineindexpage_deep_archive_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazineindexpage',
            name='featured_deep_archive_issue',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='magazine.ArchiveIssue'),
        ),
    ]