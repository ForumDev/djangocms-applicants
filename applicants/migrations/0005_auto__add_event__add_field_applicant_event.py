# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'applicants_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('begin_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('app_begin_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('app_end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'applicants', ['Event'])

        # Adding field 'Applicant.event'
        db.add_column(u'applicants_applicant', 'event',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=-1, to=orm['applicants.Event']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'applicants_event')

        # Deleting field 'Applicant.event'
        db.delete_column(u'applicants_applicant', 'event_id')


    models = {
        u'applicants.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'edit_key': ('django.db.models.fields.CharField', [], {'default': "''", 'unique': 'True', 'max_length': '100'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'unique': 'True', 'max_length': '255'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'default': '-1', 'to': u"orm['applicants.Event']"}),
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
        u'applicants.event': {
            'Meta': {'object_name': 'Event'},
            'app_begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'app_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'begin_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'})
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