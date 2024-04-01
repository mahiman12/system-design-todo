import time
from datetime import datetime, timedelta

from enums import TaskStatus
from services.task import TaskService
from services.user import UserService
from utils.logger import Logger


def print_all_tasks(all_tasks):
    for t in all_tasks:
        print(t.__dict__)
    print('______________')


def print_logs(logs):
    for log in logs:
        print(log)
    print('______________')


def print_stats(stats):
    for k, v in stats.items():
        print(k, v)
    print('______________')


def get_activity_logs():
    for k, v in Logger.activity_logs.items():
        print(k, v)
    print('______________')


if __name__ == '__main__':
    deadline = datetime.now() + timedelta(hours=2)
    eta = datetime.now() + timedelta(seconds=5)
    statistics_start_time = datetime.now() - timedelta(hours=1)
    statistics_end_time = datetime.now() + timedelta(hours=1)
    task = TaskService()
    task.run_threaded()
    user = UserService().add_user(name='Bissa', phone='958882714', email='mahiman@gmail.com', )


    print('ADDED FIRST TASK')
    task1 = task.add_task(user_id=user.id, title='Task1', deadline=deadline, description='First task',
                          tags=['tag1', 'tag2'])
    all_tasks = task.get_all_tasks()
    print_all_tasks(all_tasks)


    print('modified first task'.upper())
    task1_modify = task.modify_task(task_id=task1.task_id, status=TaskStatus.COMPLETED)
    print_all_tasks(all_tasks)


    print('added second task'.upper())
    task2 = task.add_task(user_id=user.id, title='Task2', deadline=deadline, description='Second task',
                          tags=['tag3', 'tag4'])
    print_all_tasks(all_tasks)


    task2_delete = task.remove_task(task_id=task2.task_id)
    print('removed second task'.upper())
    print_all_tasks(all_tasks)


    print('added third task'.upper())
    task3 = task.add_task(user_id=user.id, title='Task3', deadline=deadline, description='third task',
                          tags=['tag1'])
    print_all_tasks(all_tasks)


    print('list filter by tags'.upper())
    t = task.list_task_by_tags(['tag2'])
    print_all_tasks(t)


    print('activity logs'.upper())
    logs = Logger.get_logs(start_time=statistics_start_time, end_time=statistics_end_time)
    print_logs(logs)


    print('statistics'.upper())
    stats = Logger.get_statistics(start_time=statistics_start_time, end_time=statistics_end_time)
    print_stats(stats)


    print('added fourth task FUTURE task'.upper())
    task4 = task.add_task(user_id=user.id, title='Task4', deadline=deadline, description='fourth task',
                          tags=['tag4'], eta=eta)
    print_all_tasks(all_tasks)
    print('printing all tasks after 10 seconds'.upper())
    time.sleep(10)
    print_all_tasks(all_tasks)


    todolist = TaskService()