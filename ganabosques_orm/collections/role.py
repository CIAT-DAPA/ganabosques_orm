from mongoengine import Document, StringField, ListField, EmbeddedDocumentField, EnumField
from ganabosques_orm.enums.actions import Actions
from ganabosques_orm.enums.options import Options


class Role(Document):
    meta = {'collection': 'role'}

    name = StringField()

    actions = ListField(EnumField(Actions))

    options = ListField(EnumField(Options))