from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional


class Suppliers(Document):
    """Auto-generated MongoDB collection: Suppliers"""
    meta = {'collection': 'suppliers'}
    id = ObjectIdField(primary_key=True)
    enterprise_id = ObjectIdField(primary_key=True)
    farm_id = ObjectIdField(primary_key=True)
    label = StringField()