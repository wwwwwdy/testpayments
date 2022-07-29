from functools import wraps

import marshmallow_dataclass


class SchemaValidator:
    def __init__(self, schema):
        self.schema = schema

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not (data := kwargs.get("data")):
                _, data = args

            schema = marshmallow_dataclass.class_schema(self.schema)()
            schema_object = schema.load(data)
            schema_dict = {
                k: v for k, v
                in schema.dump(schema_object).items()
                if v is not None
            }
            result = func(args[0], schema_dict)
            return result

        return wrapper
