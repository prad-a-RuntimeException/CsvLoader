import sqlalchemy.types as types
from decimal import Decimal


class CustomInt(types.TypeDecorator):
    impl = types.Integer

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            try:
                return int(value)
            except:
                return 0
        return value


class CustomFloat(types.TypeDecorator):
    impl = types.Float

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            try:
                return Decimal(value)
            except:
                return 0
        return value


possible_true_values = set(["y", "1", "yes", "true"]);


class CustomBoolean(types.TypeDecorator):
    impl = types.BOOLEAN

    def process_result_value(self, value, dialect):
        return bool(int(value))

    def process_bind_param(self, value, dialect):
        if type(value) is str:
            value = value.lower()
            try:
                return True if value in possible_true_values else False
            except:
                return 0
        return value
