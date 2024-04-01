class ListFilterService:

    @staticmethod
    def order_by_created_at(*, tasks=list):
        """
        :param tasks:
        :return:
        """
        sorted_tasks = sorted(tasks, key=lambda x: x.created_at, reverse=True)
        return sorted_tasks

    @staticmethod
    def filter_by_tags(*, tags=list, tasks=list):
        """
        :param tags:
        :param tasks:
        :return:
        """
        tags_set = set(tags)
        filter_tag_list = []
        for task in tasks:
            tags_list = task.tags
            if tags_list & tags_set:
                filter_tag_list.append(task)
        return filter_tag_list

    def call_method(self, method_name, **kwargs):
        if hasattr(self, method_name):
            method = getattr(self, method_name)
            return method(**kwargs)
        else:
            raise AttributeError(f"Method {method_name} not found in ListFilter")
