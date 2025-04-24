from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class ExtIdFarm(EmbeddedDocument):
    """Auto-generated auxiliary: ExtIdFarm"""
    source = StringField()
    ext_code = StringField()