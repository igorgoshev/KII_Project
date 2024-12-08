from mongoengine import Document, StringField, BooleanField, DateTimeField
from datetime import datetime


class Task(Document):
    title = StringField(max_length=200, required=True)
    completed = BooleanField(default=False)
    created_date = DateTimeField(default=datetime.now)

    meta = {'collection': 'tasks'}

    def __str__(self):
        return self.title