from rest_flex_fields import FlexFieldsModelSerializer
from rest_framework import serializers


class AdvFlexFieldsModelSerializer(FlexFieldsModelSerializer):
    """
    Modify the mechanism of drf-flex-fields schema generation for drf-spectacular,
    """

    def get_fields(self):
        fields = super().get_fields()

        # To add additional {pk}_id fields
        new_pks = {}
        for field_name, field in fields.items():
            if isinstance(field, serializers.PrimaryKeyRelatedField):
                new_pks[f"{field_name}_id"] = field
        fields.update(new_pks)

        return fields
