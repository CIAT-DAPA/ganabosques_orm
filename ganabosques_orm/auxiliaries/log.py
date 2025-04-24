from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class Log(EmbeddedDocument):
    """Auto-generated auxiliary: Log"""
    enable = BooleanField()
    created = DateTimeField()
    updated = DateTimeField()