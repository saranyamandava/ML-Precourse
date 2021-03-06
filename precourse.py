# Machine Learning/Data Science Precourse Work

# ###
# LAMBDA SCHOOL
# ###
# MIT LICENSE
# ###

# Free example function definition
# This function passes one of the 11 tests contained inside of test.py. Write the rest, defined in README.md, here, and execute python test.py to test. Passing this precourse work will greatly increase your odds of acceptance into the program.
import numpy as np
import math
def f(x):
 return x**2

def f_2(x):
 return x**3

def f_3(x):
 return x**3+5*x

def d_f(x):
 return 2*x

def d_f_2(x):
 a = x**2
 return 3*a

def d_f_3(x):
 a = x**2
 return 3*a + 5 

def vector_sum(v1,v2):
 x = np.array(v1)
 y = np.array(v2)	
 res = x + y
 return res

def vector_less(v1,v2):
 x = np.array(v1)
 y = np.array(v2)
 res = x - y
 return res

def vector_magnitude(x):
 sum = 0
 for i in range(0, len(x)):
  sum += x[i]**2
 return(math.sqrt(sum))

def vec5():
 x = np.ones(5)
 return x

def vec3():
 x=np.zeros(3)
 return x

def vec2_1():
 a=np.array([1,0])
 return a

def vec2_2():
 a=np.array([0,1])
 return a

def matrix_multiply(m,v):
 a = np.array(m)
 b = np.array(v)
 c = a.dot(b)
 return c
 


		
