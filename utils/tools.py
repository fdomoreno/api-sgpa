import base64


class tools:

    def __init__(self):
        pass

    def validar_basic_auth(self, authbasic:str):
        try:
            auth = authbasic.split(" ")[1]
            user, password = base64.b64decode(auth).decode('utf-8').split(":")
            if user == "admin" and password == "admin":
                return True
            else:
                return False
        except Exception as e:
            return False