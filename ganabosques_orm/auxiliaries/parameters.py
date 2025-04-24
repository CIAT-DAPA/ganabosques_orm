from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class Parameters(EmbeddedDocument):
    """Auto-generated auxiliary: Parameters"""
    key = StringField()
    value = StringField()