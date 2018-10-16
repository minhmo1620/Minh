
# coding: utf-8

# In[27]:


def reverse_integer(x):
    global L
    X = ""
    L = str(x)
    a = len(L)
    if x > 0:
        for i in range (a):
            b = -i -1
            c = L[b]
            X +=c
        print(X)
    else:
        X += "-"
        for i in range (a-1):
            b = -i -1
            c = L[b]
            X +=c
        print(X)
        

reverse_integer(-123)
    
    


# In[33]:


def reverse_string(L):
    global b
    X =""
    a = len(L)
    for i in range(a):
        b = -i-1
        c = L[b]
        X += c
    print(X)
    
reverse_string("Minh xinh gai qua")


# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.
#     Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

# In[65]:


def trans_value(x):
    global A
    if x =="I":
        A = 1
    if x == "V":
        A = 5
    if x == "X":
        A = 10
    if x == "L":
        A = 50
    if x == "C":
        A = 100
    if x == "D":
        A = 500
    if x == "M":
        A = 1000
    return A
    
def trans_roman(X):
    B = 0
    C = len(X)
    global f
    for i in range (C):
        d = X[i]
        d_1 = trans_value(d)
        if i < (C-1):
            
            f = (i +1)
            e = X[f]
            
            e_1 = trans_value(e)
            if d_1 < e_1:
                d_1 = -d_1
            B +=d_1 
        else:
            B +=d_1
        
    print (B)
        
trans_roman("MCMXCIV") 

        

