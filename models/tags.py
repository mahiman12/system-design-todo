class Tags:

    def __init__(self):
        self._tags = set()

    def add_tag(self, tag: str):
        self._tags.add(tag)

    def get_all_tags(self):
        return list(self._tags)
