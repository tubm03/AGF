class Form:
    def __init__(self, url):
        self.url = url
        self.lists = []
    
    def to_dict(self):
        return {
            'url': self.url,
            'lists': [item.__json__() for item in self.lists]
        }