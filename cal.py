import random 


class LittleProf:
    def __init__(self):
        self.quiz = 10
        self.attempt = 3 
        self.score = 0
        self.Lvl = self.correctLvl()
    
    def correctLvl(self):
        while True:
            try:
                get = int(input("Select Level: [1/2/3] "))
                if get in [1, 2, 3]:
                    return get  
            except ValueError:
                print("invalid input..!")
        
    def genNum(self):
        if self.Lvl == 1:
            x = random.randint(1, 10)
            y = random.randint(1, 10)
        elif self.Lvl == 2:
            x = random.randint(10, 100)
            y = random.randint(10, 100)
        else:
            x = random.randint(100, 1000)
            y = random.randint(100, 1000)
        return x, y

    def selectOp(self):
        while True:
            print("1. +\n2. -\n3. \n4. /*")
            getOp = int(input("> "))
            if getOp == 1:
                op  ="+"
            
            elif getOp == 2:
                op = "-"
            
            elif getOp == 3:
                op = "/"
            
            else:
                op = "*"
            
            if getOp not in [1, 2, 3, 4]:
                print("invalid")
                continue
            return op 
        


    def play(self):
        getOp = self.selectOp()
        while self.quiz != 0:
            x, y = self.genNum()
            for i in range(self.attempt):
                try:               
                    ask = int(input(f"{x} {getOp} {y} = "))
                    if ask ==  eval(f"{x} {getOp} {y}"):
                        self.quiz -= 1
                        self.score += 1
                        break
                except ValueError:
                    pass 

        print(f"Score: {self.score}")
        return self.score

start = LittleProf()
start.play()