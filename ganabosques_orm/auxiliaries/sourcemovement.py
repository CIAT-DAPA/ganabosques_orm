from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class SourceMovement(EmbeddedDocument):
    """Auto-generated auxiliary: SourceMovement"""
    id = ObjectIdField(primary_key=True)
    name = StringField()
    log = StringField()