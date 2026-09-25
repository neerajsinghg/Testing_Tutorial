"""
Dynamic Type and Structure JSON Schema Validator
Senior SDET Context: Validates field data types and mandatory constraints without external third-party dependencies.
"""

def validate_schema(data: dict, schema: dict) -> list[str]:
    errors = []
    for field, expected_type in schema.items():
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
        elif not isinstance(data[field], expected_type):
            actual_type = type(data[field]).__name__
            errors.append(f"Field '{field}' should be type {expected_type.__name__}, got {actual_type}")
    return errors

if __name__ == "__main__":
    schema_definition = {
        "id": int,
        "name": str,
        "is_active": bool,
        "score": (int, float)
    }
    sample_response = {
        "id": 101,
        "name": "Neeraj",
        "is_active": "true",
    }
    schema_errors = validate_schema(sample_response, schema_definition)
    print("Schema Errors:", schema_errors)
