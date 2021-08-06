print(" S T A R T ")
class Student:
    def __init__(self,name):
        self.name=name

    def avg(self,data):
        sum=0
        for n in data:
            sum +=n
        avg =sum/len(data)
        return avg
    def judge(self,avg):
        norma=60
        if(avg >= norma):
            result="passed"
        else:
            result="failed"
        return result
a1=Student("Alice")
data=[70,65,50,90,30]
avg=a1.avg(data)
result = a1.judge(avg)
print(avg,"\n",a1.name+" "+result)