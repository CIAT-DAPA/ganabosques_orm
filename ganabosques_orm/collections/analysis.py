from mongoengine import Document, ObjectIdField, DateTimeField, ReferenceField
from ganabosques_orm.collections.protectedareas import ProtectedAreas
from ganabosques_orm.collections.farmingareas import FarmingAreas
from ganabosques_orm.collections.deforestation import Deforestation


class Analysis(Document):
    """Auto-generated MongoDB collection: Analysis"""
    meta = {'collection': 'analysis'}
    id = ObjectIdField(primary_key=True)
    protected_areas_id = ReferenceField(ProtectedAreas)
    farming_areas_id = ReferenceField(FarmingAreas)
    deforestation_id = ReferenceField(Deforestation)
    user_id = ObjectIdField()
    date = DateTimeField()