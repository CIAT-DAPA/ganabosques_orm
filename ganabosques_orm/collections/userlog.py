from mongoengine import Document, StringField, ObjectIdField, BooleanField, DateTimeField, EmbeddedDocumentField
from typing import Optional


class UserLog(Document):
    """Auto-generated MongoDB collection: UserLog"""
    meta = {'collection': 'userlog'}
    id = ObjectIdField(primary_key=True)
    user_id = ObjectIdField(primary_key=True)
    date = StringField()
    action = StringField()
    comments = StringField()