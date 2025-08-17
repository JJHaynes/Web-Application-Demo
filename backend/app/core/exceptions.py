class EntityNotFoundError(Exception):
    def __init__(self, entity_name: str, identifier: str):
        message = f"{entity_name} with identifier {identifier} not found"
        super().__init__(message)
        self.entity_name = entity_name
        self.identifier = identifier

class InvalidTokenError(Exception):
    def __init__(self, token: str):
        super().__init__(f"Token '{token}' is invalid or has expired")
        self.token = token
