import logging
from marshmallow import Schema, fields, ValidationError


class UserSchema(Schema):
    id = fields.Integer(required=True)
    userId = fields.String(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)

    def validate(self, json_data):
        self.json_data = json_data

        try:
            UserSchema().load(self.json_data)
        except ValidationError as e:
            logging.exception(e)
        else:
            logging.info("Validation is OK!")
