# Generated by Django 4.0.4 on 2022-05-26 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_rename_id_book_book_id_rename_id_school_school_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='book_id',
            new_name='book',
        ),
        migrations.RemoveField(
            model_name='student',
            name='school_id',
        ),
        migrations.AddField(
            model_name='student',
            name='school',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.school'),
        ),
    ]
