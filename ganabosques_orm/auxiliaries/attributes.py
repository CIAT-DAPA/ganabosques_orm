from mongoengine import EmbeddedDocument, FloatField

class Attributes(EmbeddedDocument):
    """Auto-generated auxiliary: Attributes"""
    def_prop = FloatField()
    def_ha = FloatField()
    def_distance = FloatField()