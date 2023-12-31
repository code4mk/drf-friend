from rest_framework import serializers

class RawQuerySerializer(serializers.Serializer):

    def generate_fields(self, data):
        from uuid import UUID
        from datetime import datetime, timezone
        if not data:
            return []

        # Get the first dictionary in the list to determine the fields
        first_data = data[0]
        the_fields = list(first_data.keys())

        for the_field in the_fields:
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

            python_type = type(first_data[the_field])
            if python_type in type_mapping:
                field_type = type_mapping[python_type]()

            self.fields[the_field] = field_type

        return the_fields
    
 
    def __init__(self, instance=None, data=None, **kwargs):
        super().__init__(instance=instance, data=data, **kwargs)
        self.generate_fields(data)
        # print(self.get_fields())
        print(self.get_meta())
        
    def get_meta(self):
        # Check if the 'Meta' attribute exists in the class and has the 'info' attribute
        if hasattr(self, 'Meta') and hasattr(self.Meta, 'fields'):
            return self.Meta.fields
        else:
            return None