from mongoengine import Document, StringField, ObjectIdField

class Role(Document):
    """Auto-generated MongoDB collection: Role"""
    meta = {'collection': 'role'}
    name = StringField()
    descr = StringField()
    permi = StringField()