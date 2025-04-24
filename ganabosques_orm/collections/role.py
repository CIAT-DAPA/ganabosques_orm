from mongoengine import Document, StringField, ObjectIdField

class Role(Document):
    """Auto-generated MongoDB collection: Role"""
    meta = {'collection': 'role'}
    id = ObjectIdField(primary_key=True)
    name = StringField()
    descr = StringField()
    permi = StringField()