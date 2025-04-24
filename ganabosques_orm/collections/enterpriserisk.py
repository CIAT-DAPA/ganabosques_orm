from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional


class EnterpriseRisk(Document):
    """Auto-generated MongoDB collection: EnterpriseRisk"""
    meta = {'collection': 'enterpriserisk'}
    id = ObjectIdField(primary_key=True)
    enterprise_id = ObjectIdField(primary_key=True)
    farmRisk_id = ObjectIdField(primary_key=True)
    criteria = StringField()
    risk_total = StringField()