class Option:
    def __init__(self, element):
        self.element = element
        self.xpath = ''
        self.label = ''
        self.percent = 0
        self.count = 0
        self.value = ''

    def __json__(self):
        return {
            'xpath': self.xpath,
            'label': self.label,
            'percent': self.percent,
            'count': self.count,
            'value': self.value
        }