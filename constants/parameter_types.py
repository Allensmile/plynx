class ParameterEnum(object):
    def __init__(self, values=None, index=-1):
        values = values or []
        self.values = values
        self.index = index

    def to_dict(self):
        return {
            'values': self.values,
            'index': self.index
        }

    @staticmethod
    def create_from_dict(obj_dict):
        parameter_enum = ParameterEnum()
        for key, value in obj_dict.iteritems():
            setattr(parameter_enum, key, value)
        return parameter_enum

    def __repr__(self):
        return 'ParameterEnum({})'.format(str(self.to_dict()))


class ParameterTypes:
    STR = 'str'
    INT = 'int'
    BOOL = 'bool'
    TEXT = 'text'
    ENUM = 'enum'

    @staticmethod
    def get_default_by_type(parameter_type):
        if parameter_type == ParameterTypes.STR:
            return ''
        if parameter_type == ParameterTypes.INT:
            return 0
        if parameter_type == ParameterTypes.BOOL:
            return False
        if parameter_type == ParameterTypes.TEXT:
            return ''
        if parameter_type == ParameterTypes.ENUM:
            return ParameterEnum()
        else:
            return None

    @staticmethod
    def value_is_valid(value, parameter_type):
        if parameter_type == ParameterTypes.STR:
            return isinstance(value, basestring)
        if parameter_type == ParameterTypes.INT:
            try:
                tmp = int(value)
            except:
                return False
            return True
        if parameter_type == ParameterTypes.BOOL:
            return isinstance(value, int)
        if parameter_type == ParameterTypes.TEXT:
            return isinstance(value, basestring)
        if parameter_type == ParameterTypes.ENUM:
            return isinstance(value, ParameterEnum)
        else:
            return False
