class V1:
    def __init__(self,about,DP):
        self.about = about
        self.DP      = DP 
    def Display(self):
        print(f'{self.about}\n{self.DP}')
class V2(V1):
    def __init__(self,about,DP,status,audiocall):
        #super().__init__(about,DP)
        V1.__init__(self,about,DP)
        self.status = status
        self.audiocall = audiocall
    def Display(self):
        #super().Display()
        V1.Display(self)
        print(f'{self.status}\n{self.audiocall}')
class V3(V2):
    def __init__(self,about,DP,status,audiocall,AI,payments):
        #super().__init__(about,DP,status,audiocall)
        V2.__init__(self,about,DP,status,audiocall)
        self.AI = AI
        self.payments = payments
    def Display(self):
        #super().Display()
        V2.Display(self)
        print(f'{self.AI} \n{self.payments}')

ob1=V3('Hey', 'Empty', 'Done', '10-minutes', 'MetaAI', '2000 maximum')
ob1.Display()