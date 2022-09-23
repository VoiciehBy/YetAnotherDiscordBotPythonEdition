import constants

class song():
    def __init__(self, title, url_suffix):
        self.title = title
        self.url = constants.ytUrl + url_suffix