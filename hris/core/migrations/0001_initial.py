# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TaxTable'
        db.create_table('core_taxtable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('status', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
            ('bracket', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('exemption', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('over', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('max_amount', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('min_amount', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
        ))
        db.send_create_signal('core', ['TaxTable'])

        # Adding model 'PaySlip'
        db.create_table('core_payslip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('start', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('salary_per_day', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('working_days', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('transportation', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('communication', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('project_honoraria', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('project_incentive', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('sss', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('philhealth', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('pagibig', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('withholding_tax', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('loan', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('others', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='payslip_created_by', to=orm['auth.User'])),
        ))
        db.send_create_signal('core', ['PaySlip'])


    def backwards(self, orm):
        
        # Deleting model 'TaxTable'
        db.delete_table('core_taxtable')

        # Deleting model 'PaySlip'
        db.delete_table('core_payslip')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 48, 84253)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 48, 84168)'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'core.payslip': {
            'Meta': {'object_name': 'PaySlip'},
            'communication': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'payslip_created_by'", 'to': "orm['auth.User']"}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loan': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'others': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'pagibig': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'philhealth': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'project_honoraria': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'project_incentive': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'salary_per_day': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'sss': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'start': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'transportation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'withholding_tax': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'working_days': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'core.taxtable': {
            'Meta': {'object_name': 'TaxTable'},
            'bracket': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'exemption': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_amount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'min_amount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'over': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'status': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        }
    }

    complete_apps = ['core']
