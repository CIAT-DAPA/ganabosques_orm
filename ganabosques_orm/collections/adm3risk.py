from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional


class Adm3Risk(Document):
    """Auto-generated MongoDB collection: Adm3Risk"""
    meta = {'collection': 'adm3risk'}
    id = ObjectIdField(primary_key=True)
    adm3_id = ObjectIdField(primary_key=True)
    analysis_id = ObjectIdField(primary_key=True)
    def_ha = StringField()
    farm_amount = StringField()
    risk_total = StringField()