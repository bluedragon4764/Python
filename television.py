class  Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2.0
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3.0
    x = 0
    y = 0
    __status = False
    __channel = 0
    __volume = 0
    __muted = False
    def __init__(self, status= False, muted = False, volume = MIN_VOLUME, channel= MIN_CHANNEL ):

        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
    def power(self):
        if self.__status == True:
            self.__status = False
        else:
            self.__status = True

         
          # how to change back
    def mute(self):
        if self.__muted == True:
            self.__muted = False
        else:
            self.__muted = True





    def channel_up(self):
        if self.__status == True and self.__channel < 3 :
            self.__channel += 1
        if  self.__channel == 3:
            self.__channel = 1


    def channel_down(self):
        if self.__status == True and self.__channel >= 0:
            self.__channel -= 1
        if  self.__channel == -1:
            self.__channel = 3



    def volume_up(self):

        if self.__status == True and self.__volume < 2 and self.y < 2 :
            self.__volume+= 1
            self.y += 1
        if self.__muted:
           self.__volume = 0

        else:
           self.__volume = self.y

    def volume_down(self):

        if self.__status == True and self.__volume >= 1 and self.y >= 1 :
            self.__volume -= 1
            self.y -= 1


        if self.__muted:
           self.__volume = 0

        else:
         self.__volume = self.y


    def __str__(self):
        return f" Power = [{self.__status}], Channel = [{self.__channel}], Volume = [{self.__volume}] "



