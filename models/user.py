import uuid


class User:

    def __init__(self, name: str, phone: str, email: str):
        """
        TODO: add validations for name, phone and email
        :param name:
        :param phone:
        :param email:
        """
        self.id = uuid.uuid4()
        self.name = name
        self.phone = phone
        self.email = email
