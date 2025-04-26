class elements:
    def sum(self , nums , target):
        dict={}
        for i , num in enumerate(nums):
            if target-num in dict:
                return(dict[target-num], i)
            dict[num]=i
value=int(input("Enter the sum"))
print("Index1=%d , index2=%d" %elements().sum((10,20,30,40,50,60,70), value))

