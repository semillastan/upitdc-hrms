# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Department'
        db.create_table('accounts_department', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 25, 0, 32, 40, 170614))),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 25, 0, 32, 40, 170644))),
        ))
        db.send_create_signal('accounts', ['Department'])

        # Adding model 'Designation'
        db.create_table('accounts_designation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Department'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 25, 0, 32, 40, 171088))),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 25, 0, 32, 40, 171115))),
        ))
        db.send_create_signal('accounts', ['Designation'])

        # Adding model 'UserProfile'
        db.create_table('accounts_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('marital_status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('personnel_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('designation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Designation'], null=True, blank=True)),
            ('official_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
        ))
        db.send_create_signal('accounts', ['UserProfile'])

        # Adding model 'ContactInformation'
        db.create_table('accounts_contactinformation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('accounts', ['ContactInformation'])

        # Adding model 'Contract'
        db.create_table('accounts_contract', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_contract', to=orm['auth.User'])),
            ('start', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('salary_per_hour', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2012, 7, 25, 0, 32, 40, 173442))),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_contract_created', to=orm['auth.User'])),
            ('last_updated', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('accounts', ['Contract'])


    def backwards(self, orm):
        
        # Deleting model 'Department'
        db.delete_table('accounts_department')

        # Deleting model 'Designation'
        db.delete_table('accounts_designation')

        # Deleting model 'UserProfile'
        db.delete_table('accounts_userprofile')

        # Deleting model 'ContactInformation'
        db.delete_table('accounts_contactinformation')

        # Deleting model 'Contract'
        db.delete_table('accounts_contract')


    models = {
        'accounts.contactinformation': {
            'Meta': {'object_name': 'ContactInformation'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'accounts.contract': {
            'Meta': {'object_name': 'Contract'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 40, 173442)'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_contract_created'", 'to': "orm['auth.User']"}),
            'end': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'salary_per_hour': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'start': ('django.db.models.fields.DateField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_contract'", 'to': "orm['auth.User']"})
        },
        'accounts.department': {
            'Meta': {'object_name': 'Department'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 40, 170614)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 40, 170644)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'accounts.designation': {
            'Meta': {'object_name': 'Designation'},
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 40, 171088)'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Department']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 40, 171115)'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'})
        },
        'accounts.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'designation': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Designation']", 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'marital_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'official_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'personnel_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
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
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 40, 189780)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2012, 7, 25, 0, 32, 40, 189699)'}),
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
        }
    }

    complete_apps = ['accounts']
