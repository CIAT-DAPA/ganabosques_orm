from mongoengine import Document, StringField, ObjectIdField, ReferenceField, DateTimeField
from ganabosques_orm.collections.user import User


class UserLog(Document):
    """Auto-generated MongoDB collection: UserLog"""
    meta = {'collection': 'userlog'}
    id = ObjectIdField(primary_key=True)
    user_id = ReferenceField(User)
    date = DateTimeField()
    action = StringField()
    comments = StringField()