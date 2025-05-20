post_schema = {
    "type": "object",
    "properties": {
        "userId": {"type": "integer"},
        "id": {"type": "integer"},
        "title": {"type": "string"},
        "body": {"type": "string"}
    },
    "required": ["userId", "id", "title", "body"]
}

comment_schema = {
    "type": "object",
    "properties": {
        "postId": {"anyOf": [{"type": "integer"}, {"type": "string"}]},  # Accept string or integer
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"},
        "body": {"type": "string"}
    },
    "required": ["postId", "id", "name", "email", "body"]
}
