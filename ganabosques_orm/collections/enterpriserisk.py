from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentListField, FloatField
from typing import Optional
from ganabosques_orm.auxiliaries.criteria import Criteria


class EnterpriseRisk(Document):
    """Auto-generated MongoDB collection: EnterpriseRisk"""
    meta = {'collection': 'enterpriserisk'}
    id = ObjectIdField(primary_key=True)
    enterprise_id = ObjectIdField(primary_key=True)
    farm_risk_id = ObjectIdField(primary_key=True)
    criteria = EmbeddedDocumentListField(Criteria)
    risk_total = FloatField()