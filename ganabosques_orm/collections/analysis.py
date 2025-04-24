from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional


class Analysis(Document):
    """Auto-generated MongoDB collection: Analysis"""
    meta = {'collection': 'analysis'}
    id = ObjectIdField(primary_key=True)
    protected_areas_id = ObjectIdField(primary_key=True)
    farming_areas_id = ObjectIdField(primary_key=True)
    deforestation_id = ObjectIdField(primary_key=True)
    user_id = ObjectIdField(primary_key=True)
    date = DateTimeField()