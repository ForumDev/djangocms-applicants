# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Applicant'
        db.create_table(u'applicants_applicant', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('firstname', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', unique=True, max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('edit_key', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'applicants', ['Applicant'])

        # Adding model 'Reference'
        db.create_table(u'applicants_reference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['applicants.Applicant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', unique=True, max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')(default='')),
            ('edit_key', self.gf('django.db.models.fields.CharField')(max_length=100, unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'applicants', ['Reference'])

        # Adding model 'Attachment'
        db.create_table(u'applicants_attachment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('applicant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['applicants.Applicant'])),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal(u'applicants', ['Attachment'])


    def backwards(self, orm):
        # Deleting model 'Applicant'
        db.delete_table(u'applicants_applicant')

        # Deleting model 'Reference'
        db.delete_table(u'applicants_reference')

        # Deleting model 'Attachment'
        db.delete_table(u'applicants_attachment')


    models = {
        u'applicants.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'edit_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        },
        u'applicants.attachment': {
            'Meta': {'object_name': 'Attachment'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']"}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'applicants.reference': {
            'Meta': {'object_name': 'Reference'},
            'applicant': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['applicants.Applicant']"}),
            'edit_key': ('django.db.models.fields.CharField', [], {'max_length': '100', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'text': ('django.db.models.fields.TextField', [], {'default': "''"})
        }
    }

    complete_apps = ['applicants']