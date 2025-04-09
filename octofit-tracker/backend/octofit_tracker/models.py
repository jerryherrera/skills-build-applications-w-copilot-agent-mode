from mongoengine import Document, StringField, ReferenceField, ListField, IntField, EmbeddedDocument, EmbeddedDocumentField, DurationField
from datetime import timedelta
from mongoengine import IntField

class User(Document):
    username = StringField(max_length=100, required=True)
    email = StringField(unique=True, required=True)
    password = StringField(max_length=100, required=True)

class Team(Document):
    name = StringField(max_length=100, required=True)
    members = ListField(ReferenceField(User))

class DurationField(IntField):
    def to_python(self, value):
        if isinstance(value, int):
            return timedelta(seconds=value)
        return value

    def to_mongo(self, value):
        if isinstance(value, timedelta):
            return int(value.total_seconds())
        return value

    def validate(self, value):
        if not isinstance(value, (timedelta, int)):
            self.error("Invalid value for DurationField. Must be timedelta or int.")
        super().validate(value)

# Update Activity model to use the custom DurationField
class Activity(Document):
    user = ReferenceField(User, required=True)
    activity_type = StringField(max_length=100, required=True)
    duration = DurationField(required=True)

class Leaderboard(Document):
    user = ReferenceField(User, required=True)
    score = IntField(required=True)

class Workout(Document):
    name = StringField(max_length=100, required=True)
    description = StringField()