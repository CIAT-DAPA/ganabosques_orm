from mongoengine import Document, ObjectIdField, DateTimeField, ReferenceField, EmbeddedDocumentField, EnumField
from ganabosques_orm.collections.protectedareas import ProtectedAreas
from ganabosques_orm.collections.farmingareas import FarmingAreas
from ganabosques_orm.collections.deforestation import Deforestation
from ganabosques_orm.enums.valuechain import ValueChain

class Analysis(Document):
    """Auto-generated MongoDB collection: Analysis"""
    meta = {'collection': 'analysis'}
    protected_areas_id = ReferenceField(ProtectedAreas)
    farming_areas_id = ReferenceField(FarmingAreas)
    deforestation_id = ReferenceField(Deforestation)
    user_id = ObjectIdField()
    date = DateTimeField()
    value_chain = EnumField(ValueChain)
