from rest_framework import serializers
from uuid import UUID
from datetime import datetime
from collections import OrderedDict

class RawQuerySerializer(serializers.Serializer):

    def generate_fields(self, data):
        the_get_fields = list(OrderedDict.fromkeys(self.get_fields()))  # ['id', 'is_active']
        meta_excepts = self.get_meta_excepts()  # Get fields to be excluded from Meta

        if not data:
            return []

        # Get the fields from the 'Meta' class or from the first data dictionary
        the_fields = self.get_meta_fields() or list(data[0].keys())

        for the_field in the_fields:
            if the_field not in the_get_fields and the_field not in meta_excepts:
                # Determine the field type based on the data type in the first dictionary
                field_type = serializers.CharField()

                # Mapping between Python types and Django model field types
                type_mapping = {
                    int: serializers.IntegerField,
                    float: serializers.FloatField,
                    str: serializers.CharField,
                    bool: serializers.BooleanField,
                    UUID: serializers.UUIDField,
                    datetime: serializers.DateTimeField,
                    list: serializers.ListField,
                    dict: serializers.DictField,
                    # Add more mappings as needed
                }

                python_type = type(data[0][the_field])
                if python_type in type_mapping:
                    field_type = type_mapping[python_type]()

                self.fields[the_field] = field_type

        # Remove fields that are not in the_get_fields and not in meta_excepts
        for the_get_field in the_get_fields:
            if the_get_field not in the_fields and the_get_field not in meta_excepts:
                del self.fields[the_get_field]

        return the_fields

    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.generate_fields(data)

    def get_meta_fields(self):
        # Check if the 'Meta' attribute exists in the class and has the 'fields' attribute
        if hasattr(self, 'Meta') and hasattr(self.Meta, 'fields'):
            return self.Meta.fields
        else:
            return None

    def get_meta_excepts(self):
        # Check if the 'Meta' attribute exists in the class and has the 'excepts' attribute
        if hasattr(self, 'Meta') and hasattr(self.Meta, 'excepts'):
            return self.Meta.excepts
        else:
            return []
