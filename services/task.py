import datetime
import threading
import time
import uuid

from enums import TaskStatus
from models.tags import Tags
from models.tasks import Tasks
from services.list_filter import ListFilterService
from utils.logger import Logger


class TaskService:

    def __init__(self):
        self._tasks = []
        self._future_tasks = []
        self.tags = set()

    @Logger.activity_logger
    def add_task(self, *, user_id: uuid, title: str, deadline: datetime, description: str = None, tags: list = None,
                 eta=None):
        """
        :param *:
        :param user_id:
        :param deadline:
        :param title:
        :param description:
        :param tags:
        :param eta:
        :return:
        """
        task = Tasks(title=title, description=description, tags=tags, deadline=deadline, user_id=user_id)
        self.update_tags(tags)
        if eta:
            self._future_tasks.append(task)
        else:
            self._tasks.append(task)
        return task

    def get_task(self, task_id):
        """
        :param task_id:
        :return:
        """
        for task in self._tasks:
            if task.task_id == task_id:
                return task
        raise Exception("Task id doesn't exist")

    @Logger.activity_logger
    def modify_task(self, *, task_id: uuid, title: str = None, description: str = None, status: TaskStatus = None,
                    tags: list = None):
        """
        :param *:
        :param task_id:
        :param title:
        :param description:
        :param status:
        :param tags:
        :return:
        """
        task = self.get_task(task_id=task_id)
        if title:
            task.title = title
        if description:
            task.description = description
        if status:
            task.status = status
        if tags:
            self.update_tags(tags)
            task.tags = tags
        task.modified_at = datetime.datetime.now()
        return task

    @Logger.activity_logger
    def remove_task(self, *, task_id: uuid):
        """
        :param *:
        :param task_id:
        :return:
        """
        task = self.get_task(task_id=task_id)
        self._tasks.remove(task)
        return task

    def get_all_tasks(self):
        return self._tasks

    def get_future_tasks(self):
        return self._future_tasks

    def list_tasks(self):
        """"""
        return ListFilterService.order_by_created_at(tasks=self._tasks)

    def list_task_by_tags(self, tags):
        """"""
        return ListFilterService.filter_by_tags(tasks=self._tasks, tags=tags)

    @staticmethod
    def update_tags(tags):
        for tag in tags:
            Tags().add_tag(tag)

    def job(self):
        while True:
            future_tasks = self._future_tasks
            curr_time = datetime.datetime.now()
            for task in future_tasks:
                if task.eta <= curr_time:
                    self.add_task(user_id=task.user_id, title=task.title, deadline=task.deadline,
                                  description=task.description, tags=task.tags)
                    self._future_tasks.remove(task)
            time.sleep(2)

    def run_threaded(self):
        job_thread = threading.Thread(target=self.job)
        job_thread.start()
