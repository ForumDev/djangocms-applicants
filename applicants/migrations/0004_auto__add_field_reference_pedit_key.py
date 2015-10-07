# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Reference.pedit_key'
        db.add_column(u'applicants_reference', 'pedit_key',
                      self.gf('django.db.models.fields.CharField')(default='', unique=True, max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Reference.pedit_key'
        db.delete_column(u'applicants_reference', 'pedit_key')


    models = {
        u'applicants.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'firstname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '25'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'applicants.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']"}),
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'applicants.reference': {
            'Meta': {'object_name': 'Reference'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']"}),
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'pedit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['applicants']