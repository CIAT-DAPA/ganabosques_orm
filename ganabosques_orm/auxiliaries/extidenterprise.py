from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class ExtIdEnterprise(EmbeddedDocument):
    """Auto-generated auxiliary: ExtIdEnterprise"""
    label = StringField()
    ext_code = StringField()