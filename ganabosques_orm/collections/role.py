from mongoengine import Document, StringField, ObjectIdField, EnumField, ListField, EmbeddedDocumentField
from ganabosques_orm.enums.actions import Actions
from ganabosques_orm.enums.options import Options
class Role(Document):
    """Auto-generated MongoDB collection: Role"""
    meta = {'collection': 'role'}
    name = StringField()
    actions = EmbeddedDocumentField(Actions)
    options = EmbeddedDocumentField(EnumField(Options))