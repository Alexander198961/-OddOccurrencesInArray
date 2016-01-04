	

list = [ 9 , 3, 9, 3 , 9 , 7 , 9 ]


def solution(A):
	
	size=len(A)
	for i in range(0,size):
		var=0
		z=i+1
		for j in range(z,len(A)): 
			if A[i] == A[j] :
				var=var+1;
				break
		if var == 0 :

			for t in range(0,i):
				if A[i] == A[t]:
					var=var+1
					break
		if var == 0:
			return A[i]

number=solution(list)
print number
