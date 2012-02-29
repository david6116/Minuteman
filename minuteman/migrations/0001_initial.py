# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Client'
        db.create_table('minuteman_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=128)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('minuteman', ['Client'])

        # Adding model 'Project'
        db.create_table('minuteman_project', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['minuteman.Client'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
            ('comments', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('minuteman', ['Project'])

        # Adding model 'Contractor'
        db.create_table('minuteman_contractor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('rate', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('minuteman', ['Contractor'])

        # Adding M2M table for field projects on 'Contractor'
        db.create_table('minuteman_contractor_projects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('contractor', models.ForeignKey(orm['minuteman.contractor'], null=False)),
            ('project', models.ForeignKey(orm['minuteman.project'], null=False))
        ))
        db.create_unique('minuteman_contractor_projects', ['contractor_id', 'project_id'])

        # Adding model 'Log'
        db.create_table('minuteman_log', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contractor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['minuteman.Contractor'])),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['minuteman.Project'])),
            ('start', self.gf('django.db.models.fields.DateTimeField')()),
            ('stop', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('minuteman', ['Log'])


    def backwards(self, orm):
        
        # Deleting model 'Client'
        db.delete_table('minuteman_client')

        # Deleting model 'Project'
        db.delete_table('minuteman_project')

        # Deleting model 'Contractor'
        db.delete_table('minuteman_contractor')

        # Removing M2M table for field projects on 'Contractor'
        db.delete_table('minuteman_contractor_projects')

        # Deleting model 'Log'
        db.delete_table('minuteman_log')


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
            'stop': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'})
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
