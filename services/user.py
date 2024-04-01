from models.user import User


class UserService:

    def __init__(self):
        self._users = []

    def add_user(self, *, name: str, phone: str, email: str):
        user = User(name=name, phone=phone, email=email)
        self._users.append(user)
        return user

    def remove_user(self, user_id):
        """
        TODO: implement later
        :param user_id:
        :return:
        """

    def modify_user(self, name: str, phone: str, email: str):
        """
        TOOD: implement later
        :param name:
        :param phone:
        :param email:
        :return:
        """
