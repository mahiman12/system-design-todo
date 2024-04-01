import datetime
import uuid

from enums import TaskStatus
from models.user import User


class Tasks:

    def __init__(self, user_id: User, deadline: datetime, title: str, tags: list = None,
                 eta: datetime.datetime = datetime.datetime.now(),
                 modified_at: datetime.datetime = datetime.datetime.now(),
                 status: TaskStatus = TaskStatus.CREATED, description: str = None):
        """
        :param user_id:
        :param deadline:
        :param title:
        :param tags:
        :param eta:
        :param modified_at:
        :param status:
        :param description:
        """
        self.task_id = uuid.uuid4()
        self.user_id = user_id
        self.title = title
        self.description = description
        self.created_at = datetime.datetime.now()
        self.modified_at = modified_at
        self.tags = tags
        self.status = status
        self.eta = eta
        self.deadline = deadline
