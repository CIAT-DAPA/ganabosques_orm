from mongoengine import EmbeddedDocument, StringField, ObjectIdField

class SourceMovement(EmbeddedDocument):
    """Auto-generated auxiliary: SourceMovement"""
    id = ObjectIdField(primary_key=True)
    name = StringField()