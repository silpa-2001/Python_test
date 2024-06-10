class MCASem3:
    def __init__(self,plrep,age):
        self.plrep= plrep
        self.age=age
    def Attend(self):
        print("Rep1 takes the attendence")
    def __str__(self):
        return f"{self.plrep}- {self.age}"
st=MCASem3("Gracen", 22)
st.Attend()
print(st)
