'''
file = open("foo")
try:
    data = file.read()
finally:
    file.close()
print data
'''
with open('foo') as file:
    data = file.read()
print data