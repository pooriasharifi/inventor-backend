from mongoengine import Document, fields,EmbeddedDocument



class Request_details(EmbeddedDocument):
    code_kala=fields.LongField()
    request_number=fields.IntField()
    recive_number=fields.IntField()


class Request_main(EmbeddedDocument):
    number_issued = fields.IntField()
    date = fields.DateField()
    detail=fields.ListField(fields.EmbeddedDocumentField(Request_details))



class Users(Document):
    user_id=fields.IntField(required=True,unique=True)
    full_name = fields.StringField(required=True)
    phone = fields.IntField(required=True, unique=True)
    state=fields.BooleanField(required=True)
    req=fields.ListField(fields.EmbeddedDocumentField(Request_main))




