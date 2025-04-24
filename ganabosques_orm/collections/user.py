from mongoengine import Document, StringField, ObjectIdField

class User(Document):
    """Auto-generated MongoDB collection: User"""
    meta = {'collection': 'user'}
    id = ObjectIdField(primary_key=True)
    email = StringField()
    string = StringField()
    role = StringField()