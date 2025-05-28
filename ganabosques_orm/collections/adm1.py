from mongoengine import Document, StringField, ObjectIdField, EmbeddedDocumentField
from ganabosques_orm.auxiliaries.log import Log
from ganabosques_orm.auxiliaries.bufferparameter import BufferParameter

class Adm1(Document):
    """Auto-generated MongoDB collection: Adm1"""
    meta = {'collection': 'adm1'}
    name = StringField()
    ext_id = StringField()
    buffer_p = EmbeddedDocumentField(BufferParameter)
    log = EmbeddedDocumentField(Log)