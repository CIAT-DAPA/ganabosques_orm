from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class Criteria(EmbeddedDocument):
    """Auto-generated auxiliary: Criteria"""
    label = StringField()
    value = BooleanField()