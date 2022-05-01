from rest_flex_fields.filter_backends import FlexFieldsFilterBackend
from rest_flex_fields.serializers import FlexFieldsSerializerMixin
from rest_framework.compat import coreapi, coreschema


class AdvFlexFieldsFilterBackend(FlexFieldsFilterBackend):
    def get_schema_fields(self, view):
        assert (
            coreapi is not None
        ), "coreapi must be installed to use `get_schema_fields()`"
        assert (
            coreschema is not None
        ), "coreschema must be installed to use `get_schema_fields()`"

        serializer_class = view.get_serializer_class()
        if not issubclass(serializer_class, FlexFieldsSerializerMixin):
            return []

        expandable_fields = getattr(serializer_class.Meta, "expandable_fields", {})
        available_fields = ",".join(list(expandable_fields.keys()))

        return [
            coreapi.Field(
                name="fields",
                required=False,
                location="query",
                schema=coreschema.String(
                    title="Selected fields",
                    description="Specify required field by comma",
                ),
                example="field1,field2,nested.field",
            ),
            coreapi.Field(
                name="omit",
                required=False,
                location="query",
                schema=coreschema.String(
                    title="Omitted fields",
                    description="Specify required field by comma",
                ),
                example="field1,field2,nested.field",
            ),
            coreapi.Field(
                name="expand",
                required=False,
                location="query",
                schema=coreschema.String(
                    title="Expanded fields",
                    description="Specify required nested items by comma",
                ),
                example=available_fields,
            ),
        ]

    def get_schema_operation_parameters(self, view):
        serializer_class = view.get_serializer_class()
        if not issubclass(serializer_class, FlexFieldsSerializerMixin):
            return []

        expandable_fields = getattr(serializer_class.Meta, "expandable_fields", {})
        available_fields = ",".join(list(expandable_fields.keys()))
        parameters = [
            {
                "name": "fields",
                "required": False,
                "in": "query",
                "description": "Specify required field by comma",
                "schema": {
                    "title": "Selected fields",
                    "type": "string",
                },
                "example": "field1,field2,nested.field",
            },
            {
                "name": "omit",
                "required": False,
                "in": "query",
                "description": "Specify required field by comma",
                "schema": {
                    "title": "Omitted fields",
                    "type": "string",
                },
                "example": "field1,field2,nested.field",
            },
            {
                "name": "expand",
                "required": False,
                "in": "query",
                "description": "Specify required field by comma",
                "schema": {
                    "title": "Expanded fields",
                    "type": "string",
                },
                "example": available_fields,
            },
        ]

        return parameters
