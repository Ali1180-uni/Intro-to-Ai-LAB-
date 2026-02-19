class dog:
    attr1 = "mammal"
    attr2 = "dog"
    def fun(self):
        print("i am a", self.attr1)
        print("i am a", self.attr2)
Roger = dog()
print(Roger.attr1)
Roger.fun()