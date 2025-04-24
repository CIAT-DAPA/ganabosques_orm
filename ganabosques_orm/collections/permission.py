from mongoengine import Document, StringField, ObjectIdField


class Permission(Document):
    """Auto-generated MongoDB collection: Permission"""
    meta = {'collection': 'permission'}
    id = ObjectIdField(primary_key=True)
    name = StringField()
    descr = StringField()