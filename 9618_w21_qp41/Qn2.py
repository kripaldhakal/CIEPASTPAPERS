class Picture:

    def __init__(self, pDes, pWidth, pHeight, pColour):
        self.__Description = pDes #String
        self.__Width = pWidth #Integer
        self.__Height = pHeight #Integer
        self.__FrameColour = pColour #String

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, new):
        self.__Description = new

Picture = []

for i in range(100):
    Picture.append(Picture("", 0, 0, ""))

