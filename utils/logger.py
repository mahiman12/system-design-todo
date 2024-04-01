import datetime

from enums import TaskStatus


class Logger:
    activity_logs = {
        'add': [],
        'modify': [],
        'removed': []
    }
    func_activity_mapper = {
        'add_task': 'add',
        'modify_task': 'modify',
        'remove_task': 'removed'
    }

    @staticmethod
    def activity_logger(func):
        def wrapper(*args, **kwargs):
            """
            :param args:
            :param kwargs:
            :return:
            """
            func_name = func.__name__
            result = func(*args, **kwargs)
            task = result
            Logger.activity_logs[Logger.func_activity_mapper[func_name]].append({
                'task': task.__dict__,
                'logged_at': datetime.datetime.now()
            })
            return result

        return wrapper

    @staticmethod
    def get_logs(start_time: datetime, end_time: datetime = datetime.datetime.now()):
        """
        :param start_time:
        :param end_time:
        :return:
        """
        activity_list = []
        for k, v in Logger.activity_logs.items():
            for log in v:
                created_at = log.get('logged_at')
                if end_time >= created_at >= start_time:
                    activity_list.append({
                        'action': k,
                        'task': log.get('task'),
                        'logged_at': log.get('logged_at')
                    })
        return activity_list

    @staticmethod
    def get_statistics(start_time, end_time):
        filtered_list = {
            'added': [],
            'completed': [],
            'spilled': []
        }
        for k, v in Logger.activity_logs.items():
            for t in v:
                task = t.get('task')
                deadline = task.get('deadline')
                created_at = task.get('created_at')
                status = task.get('status')
                if start_time <= created_at <= end_time:
                    if status == TaskStatus.CREATED and deadline < end_time:
                        filtered_list['spilled'].append(task)
                    elif status == TaskStatus.COMPLETED:
                        filtered_list['completed'].append(task)
                    elif status == TaskStatus.CREATED:
                        filtered_list['added'].append(task)
        return filtered_list
