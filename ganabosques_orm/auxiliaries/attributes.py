from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField

class Attributes(EmbeddedDocument):
    """Auto-generated auxiliary: Attributes"""
    def_prop = StringField()
    def_ha = StringField()
    def_distance = StringField()