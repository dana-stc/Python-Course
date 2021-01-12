## Python Course

- [Course 1](#course-1)
- [Course 2](#course-2)

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
