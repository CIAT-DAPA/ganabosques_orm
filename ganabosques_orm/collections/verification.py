from mongoengine import Document, ReferenceField, StringField, EmbeddedDocumentField, ListField
from ganabosques_orm.collections.user import User
from ganabosques_orm.auxiliaries.log import Log


class VerificationEntity(Document):
    """Auto-generated MongoDB collection: VerificationEntity"""
    meta = {'collection': 'verificationentity'}
    name = StringField()
    log = EmbeddedDocumentField(Log)
    users_allowed = ListField(ReferenceField(User))
