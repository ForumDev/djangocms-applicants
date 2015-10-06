# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Reference.edit_key'
        db.alter_column(u'applicants_reference', 'edit_key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100))

        # Changing field 'Applicant.edit_key'
        db.alter_column(u'applicants_applicant', 'edit_key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100))
        # Adding field 'Attachment.edit_key'
        db.add_column(u'applicants_attachment', 'edit_key',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # Changing field 'Reference.edit_key'
        db.alter_column(u'applicants_reference', 'edit_key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, null=True))

        # Changing field 'Applicant.edit_key'
        db.alter_column(u'applicants_applicant', 'edit_key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100, null=True))
        # Deleting field 'Attachment.edit_key'
        db.delete_column(u'applicants_attachment', 'edit_key')


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
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['applicants']