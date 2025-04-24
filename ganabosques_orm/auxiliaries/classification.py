from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class Classification(EmbeddedDocument):
    """Auto-generated auxiliary: Classification"""
    label = StringField()
    amount = StringField()