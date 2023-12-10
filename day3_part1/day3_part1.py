def valid(i,j,N,M):
    return i<N and i>=0 and j<M and j>=0

def check(i,j,matrix,N,M):

    for k,l in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,1],[1,-1],[-1,-1]]:
        if valid(i-k,j-l,N,M):
            ele = matrix[i-k][j-l]
            if not (ele.isdigit() or ele=='.'):
                return True

    return False

def countPN(i,j,matx,N,M):
    count = []
    for x in [-1,0,1]:
        f = True
        for k,l in [[i-x,j-1],[i-x,j],[i-x,j+1]]:
            if valid(k,l,N,M):
                ele = matx[k][l]
                if ele != 0 and f:
                    count.append(ele)
                    f = False
                elif ele ==0:
                    f = True
                
    return count

f = open('input.txt','r')

sum = 0
matrix= []
partNumbers = []

for line in f:
    matrix.append(line)

N = len(matrix)
M = len(matrix[0])-1

for i in range(N):
    partNumbers.append([0]*M)

    num = 0
    v = False
    pos = []
    for j in range(M):
        if matrix[i][j].isdigit():
            num = num*10+int(matrix[i][j])
            pos.append([i,j])
            if check(i,j,matrix,N,M):
                v=True
        else:
            if v:
                sum += num
                for i,j in pos:
                    partNumbers[i][j] = num
                v=False
            pos=[]
            num=0
    if v:
        sum+=num
        for i,j in pos:
            partNumbers[i][j] = num

sumGearRatios = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j] == '*' :
            l = countPN(i,j,partNumbers,N,M)
            if len(l) == 2:
                sumGearRatios+=l[0]*l[1]

print('sum of gear ratios',sumGearRatios)

print('sum of part numbers',sum)
