listA=[]
listB=[]
listC=[]
A_B=[]
EA_B=[]
nA_B=[]
aC_F=[]

def ellistA():
	n=int(input("Enter The No Of Students Playing Cricket"))
	for i in range (n):
		listA.append(int(input("Enter The Roll No Of Student Playing Cricket"))) 
	print("Elements of A ",listA)
	return listA	
	
def ellistB():
	m=int(input("Enter The No Of Students Playing Badmintion"))	
	for i in range (m):
		listB.append(int(input("Enter The Roll No Of Student Playing Badminton"))) 
	print("Elements of B",listB)
	return listB

def ellistC():
	l=int(input("Enter The No Of Students Playing Football"))	
	for i in range (l):
		listC.append(int(input("Enter The Roll No Of Student Playing Football"))) 
	print("Elements of C",listC)
	return listC
	
ellistA()
ellistB()
ellistC()

def AintersectionB():

	for i in listA:
		if i in listB:
			
			A_B.append(i)
	print("Playing Both Cricket & Badminton",A_B)	
		
AintersectionB()	

def EitherAorB():
	for i in listA:
		if i not in listB:
			EA_B.append(i)
	for i  in listB:
		if i not in listA:
			EA_B.append(i)
	print(EA_B)

EitherAorB()

def neitherAB():
	for i in listC:
		if i not in listA and listB:
			nA_B.append(i)
	
	print(nA_B)
		 
neitherAB()	


def candf():
	for i in listA:
		 if i not in listB:
		 	aC_F.append(i)

	for i in listC:
		if i not in listB:
			aC_F.append(i)
			
	print(aC_F)



	


