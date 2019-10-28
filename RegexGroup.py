import re


class RegexGroup:
    def __init__(self, timestamp, level, content1, content2, content3):
        self.timestamp = self.get_grouping(timestamp)
        self.level = self.get_grouping(level)
        self.content1 = self.get_grouping(content1)
        self.content2 = self.get_grouping(content2)
        self.content3 = self.get_grouping(content3)
        self.totalRegex = ""

    def set_totalRegex(self):
        valid_list = [self.timestamp, self.level, self.content1, self.content2, self.content3]
        for item in valid_list:
            if item == "()":
                valid_list.remove(item)

        totalStr = '\s*'.join(valid_list)
        self.totalRegex = re.compile(r'{0}'.format(totalStr))

    def get_grouping(self, item):
        return "(" + item + ")"
