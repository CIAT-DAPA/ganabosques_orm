from mongoengine import Document, ObjectIdField, EmbeddedDocumentListField, FloatField, ReferenceField
from ganabosques_orm.auxiliaries.criteria import Criteria
from ganabosques_orm.collections.enterprise import Enterprise
from ganabosques_orm.collections.analysis import Analysis


class EnterpriseRisk(Document):
    """Auto-generated MongoDB collection: EnterpriseRisk"""
    meta = {'collection': 'enterpriserisk'}
    enterprise_id = ReferenceField(Enterprise)
    analysis_id = ReferenceField(Analysis)
    criteria = EmbeddedDocumentListField(Criteria)
    risk_total = FloatField()