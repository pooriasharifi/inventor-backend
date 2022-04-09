from mongoengine import Document, fields


class Kala(Document):
    code_kala = fields.LongField(required=True)
    name = fields.StringField(required=True)
    volume = fields.StringField(required=True)
    status=fields.BooleanField()