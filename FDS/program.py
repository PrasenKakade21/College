FDS = []
n = int(input("Enter The no of students"))
newlist={}

for i in range(n):
    FDS.append(int(input("Enter the marks of students")))


def display():
    print(FDS)


display()


def avg():
    suma = 0
    counter = 0
    for i in FDS:
        if i == -1:
            continue
        else:
            suma = suma+ i
            counter = counter+ 1
    print("The Avg Score is =",suma // counter)


avg()

def maxi():
	max=0
	for i in FDS:
		if i>max:
			max=i
	print("Maximum Marks =", max)
maxi()


def mini():
		for i in FDS:
			if i==-1:
				continue
			else:
		 		mint=i
				break
		for i in FDS:
			if i==-1:
				continue
			else:
				if i<mint:
					mint=i
		print("Minimum Marks are",mint)
mini()



def highestfreq():
	max=0
	for i in FDS:
		if i in newlist:
			newlist[i]+=1
		else:
			newlist[i]+=1
	for j in newlist:
		if j>max:
			max=j
		else:
			print("max freq is," max)
highestfreq()

	





			
		


