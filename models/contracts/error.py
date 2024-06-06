import json

class error:
    
    def __init__(self, status, message_error,data):
        self.status = status
        self.message_error = message_error
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "message_error": self.message_error,
            "data": self.data
        }
    
    def to_json(self):
        return json.dumps(self.to_dict())
    
    def __str__(self):
        return self.to_json()
    