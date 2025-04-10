class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def move(self, offsetX, offsetY):
        self.x += offsetX
        self.y += offsetY

    def __repr__(self):
        return '(' + self.x + ', ' + self.y + ')'