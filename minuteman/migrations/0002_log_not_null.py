# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Log.stop'
        db.alter_column('minuteman_log', 'stop', self.gf('django.db.models.fields.DateTimeField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Log.stop'
        db.alter_column('minuteman_log', 'stop', self.gf('django.db.models.fields.DateTimeField')(default=0))


    models = {
        'minuteman.client': {
            'Meta': {'object_name': 'Client'},
            'comments': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'minuteman.contractor': {
            'Meta': {'object_name': 'Contractor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['minuteman.Project']", 'symmetrical': 'False'}),
            'rate': ('django.db.models.fields.FloatField', [], {})
        },
        'minuteman.log': {
            'Meta': {'object_name': 'Log'},
            'contractor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['minuteman.Contractor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['minuteman.Project']"}),
            'start': ('django.db.models.fields.DateTimeField', [], {}),
            'stop': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'minuteman.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['minuteman.Client']"}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rate': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['minuteman']
