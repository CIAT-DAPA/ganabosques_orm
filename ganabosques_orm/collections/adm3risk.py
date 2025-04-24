from mongoengine import Document, ObjectIdField, ReferenceField, FloatField, IntField
from ganabosques_orm.collections.adm3 import Adm3
from ganabosques_orm.collections.analysis import Analysis


class Adm3Risk(Document):
    """Auto-generated MongoDB collection: Adm3Risk"""
    meta = {'collection': 'adm3risk'}
    id = ObjectIdField(primary_key=True)
    adm3_id = ReferenceField(Adm3)
    analysis_id = ReferenceField(Analysis)
    def_ha = FloatField()
    farm_amount = IntField()
    risk_total = FloatField()