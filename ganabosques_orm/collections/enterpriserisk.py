from mongoengine import Document, ObjectIdField, EmbeddedDocumentListField, FloatField, ReferenceField
from ganabosques_orm.auxiliaries.criteria import Criteria
from ganabosques_orm.collections.enterprise import Enterprise

class EnterpriseRisk(Document):
    """Auto-generated MongoDB collection: EnterpriseRisk"""
    meta = {'collection': 'enterpriserisk'}
    id = ObjectIdField(primary_key=True)
    enterprise_id = ReferenceField(Enterprise)
    criteria = EmbeddedDocumentListField(Criteria)
    risk_total = FloatField()