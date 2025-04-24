from mongoengine import EmbeddedDocument, BooleanField, EnumField
from ganabosques_orm.enums.criteriaenum import CriteriaEnum

class Criteria(EmbeddedDocument):
    """Auto-generated auxiliary: Criteria"""
    label = EnumField(CriteriaEnum)
    value = BooleanField()