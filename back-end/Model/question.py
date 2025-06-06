class Question:
    def __init__(self, element):
        self.element = element
        self.xpath = ''
        self.type = ''
        self.heading = ''
        self.options = []
        self.scale = []
        self.rows = []
        self.columns = []

    def __json__(self):
        return {
            "xpath": self.xpath,
            "type": self.type,
            "heading": self.heading,
            "options": [option.__json__() for option in self.options],
            "scale": self.scale,
            "rows": self.rows,
            "columns": self.columns
        }