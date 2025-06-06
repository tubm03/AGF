class Button:
    def __init__(self, value, xpath):
        self.value = value
        self.xpath = xpath
    def __json__(self):
        return {
            'value': self.value,
            'xpath': self.xpath
        }