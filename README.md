## Python Course

- [Course 1 - Intro](#course-1)
- [Course 2 - Lists and Tuples](#course-2)
- [Course 3 - Sets and Dictionaries](#course-3)

### Course 1

- a variable can change its type during execution time
```python
my_var = 10 # x is an int
my_var = "now I am a string"
```
Basic Types
```python
var = 99999999999999999999999999999 # long
var = 1.23 # float
var = 1.2j # complex
var = True # bool
var = None # like Null
print(x, type(x))
```
Numerical operations
```python
x = 10+20*3.0 # x will be 70.0, float
x = 2**8 # equivalent to pow, x will be 256
x = int(10.123) # x will be 10
x = float(10) # x will be a float with value 10.0
```
```python
x = 10.0/3 # 3.3333 (float)
x = 10/3 # 3.3333 (float)
x = 10//3 # 3 (int)
```
```python
x = 0xFFFFFFF # biggest unsigned int
x = ( x + x ) & 0xFFFFFFF # not overcomer
```
```python
x = 10 < 20 > 15 # True
```
String types
```python
s = 'a string with \nlines'
s = r"also a string without \nlines" # just a string
s = """multi-line
string
"""
```
```python
x = "Name: %8s Grade: %d"%('Ion', 10)
x = "Grade: %d"%10"
s = str(10) # toString alike
s = repr(10.25)
s = "Name: %(name)8s Grade: %(student_grade)d" % {"name":"Ion","student_grade":10}
s = "Python"\
"Exam" # s is PythonExam
```
```python
a = 100
s = f"A = {a}" # s will be 'A=100'
s = f"A = {a+10}" # s will be 'A=110'
s = f"A = {float(a)}" # s will be 'A=100.0'
s = f"A = {float(a):10}" # s will be 'A=          100.0' (preceded by spaces)
s = f"A = {hex(a)}" # s will be 'A=0x64'
```
Special characters: !s = str, !r = repr, !a = ascii
```python
s = "PythonExam"
s[-1] # m
s[:3] # Pyt
s[4:] # onExam"
s[2:-4] # "thon"
s[1:7:2] # "yhn" ( 2 is the step )
len(s) # 10
```
```python
s = "A"+"12"*3 #A121212
"A" in "Python" # False
```
String functions: Str.endswith("..."), Str.startswith("..."), Str.replace(toFind, replace, [count]), Str.index(toFind), 
Str.rindex(toFind), lower(), upper(), strip(), tstrip(), format(), isalpha(), isupper(), islower(), find(...), count(...), etc.
```python
s = "AB||CD||EF||GH"
s.split("||")[2] # EF
s.split("||", 1)[0] # the second parameter tells the function to stop after 1 splits
s.split("||", 2)[2] # EF||GH
```
Other functions for Srings: 
```python
chr(65) # A
ord('A') # 65
oct, hex, format
```
If statements:
```python
if a>b: a=a+b ; b=b+a # but not recommended

if a>b:
      a=a+b
elif b>a: # equivalent to switch which is not present in python
      b=b+a
else:
      a=a*b
```
While:
```python
while a>0:
      a=a-1
      if a==2: break # will not enter in else
else:
      print("Done")
```
Equivalent of Do....While
```python
while a>10:
      x=x-1
else:
      x=x-1
```
For statement - equivalent to a forEach
```python
for index in range (0,8,3):
      print(index)
else:
      print("Done")
```
Functions
- are void if not return anything
```python
def myFunc (x,y,z):
      return x*100+y*10+z
print(myFunc(z=1,y=2,x=3)) # 321

def myFunc (x,y=6,z=7):
      return x*100+y*10+z
print(myFunc(1, 9)) # 197
```
```python
x = 10
def ModifyX ():
      x=100
ModifyX()
print(x) # 10

x = 10
def ModifyX ():
      global x
      x=100
ModifyX()
print(x) # 100
```
```python
def multi_sum (*list_numbers):
      """
      Function documentation
      """
      s=0
      for number in list_numbers:
          s+=number
      return s
print(multi_sum(1,2,3)) # 6
print(multi_sum()) # 0
```

### Course 2
***Lambda functions*** - used for filtering, sorting
```python
def addition(x,y):
      return x+y
print(addition(3,5))

addition = lambda x,y: x+y
print(addition(3,5))
```
```python
# closures
def CreateDivizibleCheckFunction(n):
      return lambda x: x%n==0
fnDiv2 = CreateDivizibleCheckFunction(2)
fnDiv7 = CreateDivizibleCheckFunction(7)
x = 14
print(x, fnDiv2(x), fnDiv7(x))  # 14 True True
```
***Sequences***:
- *list* = mutable vector ( elements can be added, deleted, etc )
- *tuple* = immutable vector ( constant list ) addition, deletion, etc operation cannot be used on this type of object
```python
x = list() # x is an empty list
x = [] # x is an empty list
x = [10,20,"test"]
x = [10,]
x = [1,2] * 5 # x is a list containnig [1,2, 1,2, 1,2, 1,2, 1,2 ]
x,y = [1,2] # x is 1, y is 2
```
```python
x = tuple() # x is an empty tuple
x = () # x is an empty tuple
x = (10,20,"test") # x is a tuple
x = 10,20,"test" # x is a tuple
x = (10,)  # x is a tuple containnig 10
x = (1,2) * 5 # x is a tuple containnig (1,2, 1,2, 1,2, 1,2, 1,2)
x = 1,2*5  # x is a tuple containing (1,10)
x,y = (1,2) # x is 1, y is 2
```
```python
x = ['A', 'B', 2, 3, 'C']
x[0] # A
x[-2] # 3
x[:3] # ['A', 'B', 2]
x[3:] # [3, 'C']
x[1:3] # 'B', 2]
x[1:-3] # ['B']
```
```python
x = ['A', 'B', 2, 3, 'C']
y = tuple(x) # y = ('A', 'B', 2, 3, 'C') 
# and vice versa

x = ('A', 2)
y = ('B', 3)
z = x + y # z = ('A', 2, 'B', 3)
# and vice versa
# BUT you cannot add a tuple and a list !!!
```
Tuples are usually used to return multiple values from a function.
```python
def ComputeSumAndProduct(*list_of_numbers):
      s = 0
      p = 1
      for i in list_of_numbers:
            s += i
            p *= i
      return (s,p)
suma,produs = ComputeSumAndProduct(1,2,3,4,5)
#suma =15, produs = 120
```
```python
x = ([1,2,3], (4,5,6)) #matrix subcomponents don’t have to be of the same type
x = ( ((1,2,3), (4,5,6)), ((7,8), (9,10,11, 12)) ) #a matrix does not have to have the same number of elements on each dimension
#the same rules from tuples apply to lists as well
x = [[1,2,3], [4,5,6]]
```
```python
for i in (1,2,3,4,5):
      print(i)
      
x = [1,2,3,4,5]
len(x) # 5
```
With *enumerate* you can get also the index together with the value
```python
for index,name in enumerate(["Dragos","Mihai","Nicu","Vlad"], 2): # 2 specify from which index the first element starts
      print("Index:%d => %s"%(index,name))
```
***Lists and Functional Programming***
```python
x = [i for i in range(1,10)] #x = [1,2,3,4,5,6,7,8,9]
x = [i for i in range(1,100) if i % 23 == 0] #x = [23, 46, 69, 92]
x = [i*i for i in range(1,6)] #x = [1, 4, 9, 16, 25]
```
```python
x=[[x, y] for x in range(1,10) for y in range(1,10) if (x+y)%7==0]
#x = [[1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [5, 9], [6, 1],
# [6, 8], [7, 7], [8, 6], [9, 5]]

x=[(x, y) for x in range(1,10) for y in range(1,10) if (x+y)%7==0]
#x = [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (5, 9), (6, 1),
# (6, 8), (7, 7), (8, 6), (9, 5)]

x=[x for x in range(2,100) if len([y for y in range(2,x//2+1) if x % y==0])==0]
#x = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
# 59, 61, 67, 71, 73, 79, 83, 89, 97]
```
Functional Programming is not fast neither performant!
```python
x = [1,2,3]
x.append(4)
x+=[5] # most used
x+= [6,7]
x+= (8,9,10) # add tuple to a list
x[len(x):] = [11]
x.extend([12,13])
x.extend((14,15))

x = [1,2,3] 
x.insert(1,"A") #x = [1, ”A”, 2, 3]
x.insert(-1,"B") #x = [1, ”A”, 2, ”B”, 3] # BEFORE last element
x.insert(len(x),"C") #x = [1, ”A”, 2, ”B”, 3, ”C”] 
```
```python
x = [1,2,3,4,5] 
x[2] = 20 #x = [1, 2, 20, 4, 5]
x[3:] = ["A","B","C"] #x = [1, 2, 20, ”A”, ”B”, ”C”]
x[:4] = [10] #x = [10, ”B”, ”C”]
x[1:3] = ['x','y','z'] #x = [10, ”x”, ”y”, ”z”]
```
```python
x = [1,2,3] 
x.remove(1) # remove first element with that value
x.remove(100) # ERROR

x = [1,2,3,4,5]
del x[2] # deletes 3
del x[-1] # deletes last element
x = [1,2,3,4,5]
del[:2] # 3,4,5
del x[2:4] # 1,2,5

x = [1,2,3,4,5]
y = x.pop(2) # [1,2,4,5]
y = x.pop() # [1,2,4]

del x[:] # x = []
x.clear()
```
```python
x = [1,2,3]
y = x # it receives a reference to x !!!!!!!
y.append(10)
#x = [1,2,3,10]
#y = [1,2,3,10]

x = [1,2,3]
y = list (x)
y.append(10)
#x = [1,2,3]
#y = [1,2,3,10]

x = [1,2,3] 
b = x.copy() #x = [1, 2, 3] b = [1, 2, 3]
b += [4] #x = [1, 2, 3] b = [1, 2, 3, 4]

x = [1,2,3] 
b = x[:] #x = [1, 2, 3] b = [1, 2, 3]
b += [4] #x = [1, 2, 3] b = [1, 2, 3, 4]
```
```python
x = ["A","B","C","D"] 
y = x.index("C") #y = 2
y = x.index("Y") #!!! ERROR !!!

x = ["A","B","C","D"] #x = [”A”, ”B”, ”C”, ”D”, ”E”]
y = "C" in x #y = True
y = "Y" in x #y = False
```
```python
x = [1,2,3,2,5,3,1,2,4,2] 
y = x.count(2) #y = 4 [1,2,3,2,5,3,1,2,4,2]
y = x.count(0)

x = [1,2,3] 
x.reverse () #x = [3,2,1]
```
```python
x = [2,1,4,3,5]
x.sort() #x = [1,2,3,4,5]
x.sort(reverse=True) #x = [5,4,3,2,1]
x.sort(key = lambda i: i%3) #x = [3,1,4,2,5]
x.sort(key = lambda i: i%3,reverse=True) #x = [5,2,4,1,3]
```
```python
x = [1,2,3,4,5]
y = list(map(lambda element: element**element,x)) #y = [1,4,9,16,25]

x = [1,2,3]
y = [4,5,6]
z = list(map(lambda e1,e2: e1+e2,x,y)) #z = [5,7,9]
```
```python
x = [1,2,3,4,5]
y = list(filter(lambda element: element%2==0,x)) #y = [2,4]
```
```python
x = list(map(lambda x: x*x, range(1,10)))
#x = [1, 4, 9, 16, 25, 36, 49, 64, 81]

x = list(filter(lambda x: x%7==1,range(1,100)))
#x = [1, 8, 15, 22, 29, 36, 43, 50, 57, 64, 71, 78, 85, 92, 99]
```
```python
x = [1,2,3,4,5]
y = max (x) #y = 5
y = max (1,3,2,7,9,3,5) #y = 9
y = max (x,key = lambda i: i % 3) #y = 2

x = [1,2,3,4,5]
y = sum (x) #y = 15
y = sum (x,100) #y = 115 (100+15)
x = [1,2,”3”,4,5]
y = sum (x) #ERROR→ Can’t add int and string
```
```python
x = [2,1,4,3,5]
y = sorted (x) #y = [1,2,3,4,5]
y = sorted (x,reverse=True) #y = [5,4,3,2,1]
y = sorted (x,key = lambda i: i%3) #y = [3,1,4,2,5]
y = sorted (x,key = lambda i: i%3,reverse=True) #y = [2,5,1,4,3]
```
```python
x = [2,1,4,3,5]
y = list (reversed(x)) #y = [5,3,4,1,2]

x = [2,1,0,3,5]
y = any(x) #y = True, all numbers except 0 are evaluated to True - OR 
y = all(x) #y = False, 0 is evaluated to False - AND
```
```python
x = [1,2,3]
y = [10,20,30]
z = list(zip(x,y)) #z = [(1,10) , (2,20) , (3,30)]

x = [(1,2) , (3,4) , (5,6)]
a,b = zip(*x) #a = (1,3,5) and b = (2,4,6)
```
```python
x = [1,2,3]
del x
print (x) #!!!ERROR!!! x no longer exists
```
### Course 3
