"""
Øving på å lage en bot som kan skrive en tekst bassert på treningsdate,
etterhvert som jeg legger til flere funksjoner, skal programmet bli bedre og bedre.
"""

try:
   f = open("filename.txt", 'r')
   cont = f.read()
   print(cont)

finally:
   f.close()