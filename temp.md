{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "lat": {
            "type": "number"
        },
        "lon": {
            "type": "number"
        },
        "rotation": {
            "type": "string"
        },
        "riceRegion": {
            "type": "string"
        },
        "detail": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "sowingDate": {
                        "type": "string"
                    },
                    "cultiType": {
                        "type": "integer"
                    },
                    "subsType": {
                        "type": "string"
                    },
                    "maturType": {
                        "type": "string"
                    },
                    "sowingMtd": {
                        "type": "integer"
                    },
                    "transpDate": {
                        "type": "string"
                    },
                    "apprCultiType": {
                        "type": "integer"
                    }
                },
                "additionalProperties": false,
                "required": [
                    "sowingDate",
                    "cultiType",
                    "subsType",
                    "maturType",
                    "sowingMtd",
                    "apprCultiType"
                ]
            }
        }
    },
    "additionalProperties": false,
    "required": [
        "lat",
        "lon",
        "rotation",
        "riceRegion",
        "detail"
    ]
}