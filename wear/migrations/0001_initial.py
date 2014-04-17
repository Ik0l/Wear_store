# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'wear_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'wear', ['Category'])

        # Adding model 'Size'
        db.create_table(u'wear_size', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Category'])),
        ))
        db.send_create_signal(u'wear', ['Size'])

        # Adding model 'Cloth'
        db.create_table(u'wear_cloth', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Category'])),
            ('rating_1', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_2', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_3', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_4', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('rating_5', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'wear', ['Cloth'])

        # Adding model 'SizeCount'
        db.create_table(u'wear_sizecount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Size'])),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Cloth'])),
            ('count', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'wear', ['SizeCount'])

        # Adding model 'Gallery'
        db.create_table(u'wear_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Cloth'])),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'wear', ['Gallery'])

        # Adding model 'Comments'
        db.create_table(u'wear_comments', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=True, db_index=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Cloth'])),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'wear', ['Comments'])

        # Adding model 'Cart'
        db.create_table(u'wear_cart', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('addres', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('comments', self.gf('django.db.models.fields.TextField')()),
            ('total', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'wear', ['Cart'])

        # Adding model 'Contacts'
        db.create_table(u'wear_contacts', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('addres', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal(u'wear', ['Contacts'])

        # Adding model 'Proxy'
        db.create_table(u'wear_proxy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Cloth'])),
            ('cart', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Cart'])),
            ('count', self.gf('django.db.models.fields.IntegerField')()),
            ('size', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wear.Size'])),
        ))
        db.send_create_signal(u'wear', ['Proxy'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'wear_category')

        # Deleting model 'Size'
        db.delete_table(u'wear_size')

        # Deleting model 'Cloth'
        db.delete_table(u'wear_cloth')

        # Deleting model 'SizeCount'
        db.delete_table(u'wear_sizecount')

        # Deleting model 'Gallery'
        db.delete_table(u'wear_gallery')

        # Deleting model 'Comments'
        db.delete_table(u'wear_comments')

        # Deleting model 'Cart'
        db.delete_table(u'wear_cart')

        # Deleting model 'Contacts'
        db.delete_table(u'wear_contacts')

        # Deleting model 'Proxy'
        db.delete_table(u'wear_proxy')


    models = {
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
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'wear.cart': {
            'Meta': {'object_name': 'Cart'},
            'addres': ('django.db.models.fields.TextField', [], {}),
            'comments': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['wear.Cloth']", 'through': u"orm['wear.Proxy']", 'symmetrical': 'False'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'total': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'wear.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'wear.cloth': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Cloth'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Category']"}),
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'rating_1': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_2': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_3': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_4': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'rating_5': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sizez': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['wear.Size']", 'through': u"orm['wear.SizeCount']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'wear.comments': {
            'Meta': {'object_name': 'Comments'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Cloth']"}),
            'text': ('django.db.models.fields.TextField', [], {})
        },
        u'wear.contacts': {
            'Meta': {'ordering': "('user',)", 'object_name': 'Contacts'},
            'addres': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'wear.gallery': {
            'Meta': {'object_name': 'Gallery'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Cloth']"})
        },
        u'wear.proxy': {
            'Meta': {'ordering': "('item',)", 'object_name': 'Proxy'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Cart']"}),
            'count': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Cloth']"}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Size']"})
        },
        u'wear.size': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Size'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Category']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'wear.sizecount': {
            'Meta': {'ordering': "('size',)", 'object_name': 'SizeCount'},
            'count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Cloth']"}),
            'size': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['wear.Size']"})
        }
    }

    complete_apps = ['wear']