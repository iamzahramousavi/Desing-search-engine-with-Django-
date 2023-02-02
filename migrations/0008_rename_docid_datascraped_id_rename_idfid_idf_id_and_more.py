# Generated by Django 4.1.4 on 2023-01-21 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("context", "0007_rename_id_datascraped_docid_rename_id_idf_idfid_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="datascraped",
            old_name="docId",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="idf",
            old_name="idfId",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="tfidflist",
            old_name="tfIdfId",
            new_name="id",
        ),
        migrations.RenameField(
            model_name="tokens",
            old_name="tokId",
            new_name="id",
        ),
    ]
