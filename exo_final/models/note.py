from datetime import datetime


class Note:
    id: int
    content: str
    creationDateTs: float
    isChecked: bool
    checkDateTs: int

    def __init__(self, id: int, content: str, isChecked: bool = False, creationDateTs: float = int(round(datetime.now().timestamp())),checkDateTs=None):
        self.id = id
        self.content = content
        self.isChecked = isChecked
        self.creationDateTs = creationDateTs
        self.checkDateTs=checkDateTs

    def check_note(self):
        if not self.isChecked:
            self.isChecked = True
            self.checkDateTs = int(round(datetime.now().timestamp()))

    def calculate_amount_of_time(self) -> str:
        diff  = datetime.now() - datetime.fromtimestamp(self.creationDateTs)
        second_diff = diff.seconds
        day_diff = diff.days
        if day_diff == 0:
            if second_diff < 10:
                return "just now"
            if second_diff < 60:
                return str(round(second_diff)) + " seconds ago"
            if second_diff < 120:
                return "a minute ago"
            if second_diff < 3600:
                return str(round(second_diff / 60)) + " minutes ago"
            if second_diff < 7200:
                return "an hour ago"
            if second_diff < 86400:
                return str(round(second_diff / 3600)) + " hours ago"
        if day_diff == 1:
            return "Yesterday"
        if day_diff < 7:
            return str(round(day_diff)) + " days ago"
        if day_diff < 31:
            return str(round(day_diff / 7)) + " weeks ago"
        if day_diff < 365:
            return str(round(day_diff / 30)) + " months ago"
        return str(round(day_diff / 365)) + " years ago"
