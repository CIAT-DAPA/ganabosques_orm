from mongoengine import Document, ReferenceField, StringField, EmbeddedDocumentField, ListField
from ganabosques_orm.collections.user import User
from ganabosques_orm.auxiliaries.log import Log


class Entity(Document):
    """Auto-generated MongoDB collection: Entity"""
    meta = {'collection': 'entity'}
    name = StringField()
    log = EmbeddedDocumentField(Log)
    users_allowed = ListField(ReferenceField(User))
