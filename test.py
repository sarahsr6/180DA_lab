from subprocess import run
from time import sleep

for i in range(10):
  print("booooo class")
  sleep(1)

if __name__=='__main__':
	x = "ECE_180_DA_DB"
	if x == "EE_180_DA_DB":
		print("You are living in 2017")
	else:
		x = x + " - Best Class Ever woooooooooo"
		print(x)
