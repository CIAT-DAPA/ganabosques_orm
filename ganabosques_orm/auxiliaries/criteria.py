from mongoengine import EmbeddedDocument, StringField, ObjectIdField, BooleanField, DateTimeField, EnumField
from ganabosques_orm.enums.criteriaenum import CriteriaEnum

class Criteria(EmbeddedDocument):
    """Auto-generated auxiliary: Criteria"""
    label = EnumField(CriteriaEnum)
    value = BooleanField()