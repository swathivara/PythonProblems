#Write a Python program that prints each item and its corresponding type from the following list.
#Sample List : datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]
for item in datalist:
  print("type of", item ,"is", type(item))
  
"""  
Output:
type of 1452 is <class 'int'>
type of 11.23 is <class 'float'>
type of (1+2j) is <class 'complex'>
type of True is <class 'bool'>
type of w3resource is <class 'str'>
type of (0, -1) is <class 'tuple'>
type of [5, 12] is <class 'list'>
type of {'class': 'V', 'section': 'A'} is <class 'dict'>
"""
