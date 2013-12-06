# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Resume'
        db.create_table(u'cmsplugin_resume', (
            (u'cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('owner', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal(u'cmsplugin_resume', ['Resume'])

        # Adding model 'WorkExperience'
        db.create_table(u'cmsplugin_resume_workexperience', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('startdate', self.gf('django.db.models.fields.DateField')()),
            ('enddate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('description', self.gf('djangocms_text_ckeditor.fields.HTMLField')(blank=True)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_resume.Resume'])),
            ('skills', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'cmsplugin_resume', ['WorkExperience'])

        # Adding model 'Education'
        db.create_table(u'cmsplugin_resume_education', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('startdate', self.gf('django.db.models.fields.DateField')()),
            ('enddate', self.gf('django.db.models.fields.DateField')()),
            ('degree', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('field_of_study', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('resume', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_resume.Resume'])),
        ))
        db.send_create_signal(u'cmsplugin_resume', ['Education'])


    def backwards(self, orm):
        # Deleting model 'Resume'
        db.delete_table(u'cmsplugin_resume')

        # Deleting model 'WorkExperience'
        db.delete_table(u'cmsplugin_resume_workexperience')

        # Deleting model 'Education'
        db.delete_table(u'cmsplugin_resume_education')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        u'cmsplugin_resume.education': {
            'Meta': {'object_name': 'Education'},
            'degree': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'enddate': ('django.db.models.fields.DateField', [], {}),
            'field_of_study': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_resume.Resume']"}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'startdate': ('django.db.models.fields.DateField', [], {})
        },
        u'cmsplugin_resume.resume': {
            'Meta': {'object_name': 'Resume', 'db_table': "u'cmsplugin_resume'", '_ormbases': ['cms.CMSPlugin']},
            u'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'owner': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'cmsplugin_resume.workexperience': {
            'Meta': {'object_name': 'WorkExperience'},
            'company': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'description': ('djangocms_text_ckeditor.fields.HTMLField', [], {'blank': 'True'}),
            'enddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'resume': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['cmsplugin_resume.Resume']"}),
            'skills': ('django.db.models.fields.TextField', [], {}),
            'startdate': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['cmsplugin_resume']