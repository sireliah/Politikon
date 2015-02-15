# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.small_image'
        db.add_column(u'events_event', 'small_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Event.big_image'
        db.add_column(u'events_event', 'big_image',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True),
                      keep_default=False)

        # Adding field 'Event.is_featured'
        db.add_column(u'events_event', 'is_featured',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Event.outcome'
        db.add_column(u'events_event', 'outcome',
                      self.gf('django.db.models.fields.PositiveIntegerField')(null=True),
                      keep_default=False)

        # Deleting field 'Transaction.outcome'
        db.delete_column(u'events_transaction', 'outcome')

        # Deleting field 'Transaction.direction_buy'
        db.delete_column(u'events_transaction', 'direction_buy')

        # Adding field 'Transaction.type'
        db.add_column(u'events_transaction', 'type',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Transaction.quantity'
        db.add_column(u'events_transaction', 'quantity',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.small_image'
        db.delete_column(u'events_event', 'small_image')

        # Deleting field 'Event.big_image'
        db.delete_column(u'events_event', 'big_image')

        # Deleting field 'Event.is_featured'
        db.delete_column(u'events_event', 'is_featured')

        # Deleting field 'Event.outcome'
        db.delete_column(u'events_event', 'outcome')

        # Adding field 'Transaction.outcome'
        db.add_column(u'events_transaction', 'outcome',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Transaction.direction_buy'
        db.add_column(u'events_transaction', 'direction_buy',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Transaction.type'
        db.delete_column(u'events_transaction', 'type')

        # Deleting field 'Transaction.quantity'
        db.delete_column(u'events_transaction', 'quantity')


    models = {
        u'events.bet': {
            'Meta': {'object_name': 'Bet'},
            'bought': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bought_avg_price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            'has': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'outcome': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rewarded_total': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            'sold': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'sold_avg_price': ('django.db.models.fields.FloatField', [], {'default': '0'}),
            # 'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fandjango.User']"})
        },
        u'events.event': {
            'B': ('django.db.models.fields.FloatField', [], {}),
            'Meta': {'object_name': 'Event'},
            'Q_against': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'Q_for': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'big_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'current_buy_price': ('django.db.models.fields.FloatField', [], {'default': '50.0'}),
            'current_sell_price': ('django.db.models.fields.FloatField', [], {'default': '50.0'}),
            'descrition': ('django.db.models.fields.TextField', [], {}),
            'estimated_end_date': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_transaction_date': ('django.db.models.fields.DateTimeField', [], {}),
            'outcome': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'short_title': ('django.db.models.fields.TextField', [], {}),
            'small_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'events.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['events.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'type': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            # 'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['fandjango.User']"})
        }
        # u'fandjango.oauthtoken': {
        #     'Meta': {'object_name': 'OAuthToken'},
        #     'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
        #     u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
        #     'issued_at': ('django.db.models.fields.DateTimeField', [], {}),
        #     'token': ('django.db.models.fields.TextField', [], {})
        # },
        # u'fandjango.user': {
        #     'Meta': {'object_name': 'User'},
        #     'authorized': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
        #     'birthday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
        #     'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
        #     'facebook_id': ('django.db.models.fields.BigIntegerField', [], {'unique': 'True'}),
        #     'facebook_username': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
        #     'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
        #     u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
        #     'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
        #     'last_seen_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
        #     'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
        #     'oauth_token': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['fandjango.OAuthToken']", 'unique': 'True'})
        # }
    }

    complete_apps = ['events']