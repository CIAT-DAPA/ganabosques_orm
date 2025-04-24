from mongoengine import Document, ObjectIdField, EmbeddedDocumentField, FloatField, ReferenceField
from ganabosques_orm.auxiliaries.attributes import Attributes
from ganabosques_orm.collections.farm import Farm
from ganabosques_orm.collections.farmpolygons import FarmPolygons

class FarmRisk(Document):
    """Auto-generated MongoDB collection: FarmRisk"""
    meta = {'collection': 'farmrisk'}
    id = ObjectIdField(primary_key=True)
    farm_id = ReferenceField(Farm)
    farm_polygons_id = ReferenceField(FarmPolygons)
    deforestation = EmbeddedDocumentField(Attributes)
    protected = EmbeddedDocumentField(Attributes)
    risk_direct = FloatField()
    risk_input = FloatField()
    risk_output = FloatField()
    risk_total = FloatField()