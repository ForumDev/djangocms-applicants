# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Note.created_at'
        db.alter_column(u'applicants_note', 'created_at', self.gf('django.db.models.fields.DateTimeField')())

    def backwards(self, orm):

        # Changing field 'Note.created_at'
        db.alter_column(u'applicants_note', 'created_at', self.gf('django.db.models.fields.DateField')())

    models = {
        u'applicants.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Event']", 'null': 'True', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'applicants.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']", 'blank': 'True'}),
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'applicants.event': {
            'Meta': {'object_name': 'Event'},
            'abbr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'}),
            'app_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'app_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
        },
        u'applicants.note': {
            'Meta': {'object_name': 'Note'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']", 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2015, 10, 7, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myauth.User']", 'blank': 'True'})
        },
        u'applicants.reference': {
            'Meta': {'object_name': 'Reference'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']", 'blank': 'True'}),
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'pedit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'applicants.score': {
            'Meta': {'object_name': 'Score'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']", 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['myauth.User']", 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'myauth.interest': {
            'Meta': {'object_name': 'Interest'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'})
        },
        u'myauth.user': {
            'Meta': {'object_name': 'User'},
            'accept_terms': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'address': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'affiliation': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "''", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'bill_address': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'department': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'facebook': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'unspecified'", 'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'google_plus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'google_scholar': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'interests': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'users'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['myauth.Interest']"}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'news_feed': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'orcid_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'personal_email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'receive_newsletter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'research_field': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'research_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'short_bio': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'supervisor': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'telephone': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['applicants']