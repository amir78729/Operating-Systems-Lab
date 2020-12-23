import numpy as np

def check(i):
    for j in range(number_of_resources):
        if(needed[i][j] > available[j]):
            return False
    return True

def print_data():
    print("\tALLOCATION\t\t\t\tNEEDED\t\t\t\t\tAVAILABLE")
    print("\t{}\t{}\t{}\t{}\t\t\t{}\t{}\t{}\t{}\t\t{}\t{}\t{}\t{}".format(resources[0],resources[1],resources[2],resources[3], resources[0],resources[1],resources[2],resources[3],  
                                                                                    resources[0],resources[1],resources[2],resources[3]))
    print("P0\t{}\t{}\t{}\t{}\t\tP0\t{}\t{}\t{}\t{}\t\t{}\t{}\t{}\t{}\t\t".format(allocation[0][0],allocation[0][1],allocation[0][2],allocation[0][3],  
                                                                                    needed[0][0],needed[0][1],needed[0][2],needed[0][3],
                                                                                    available[0],available[1],available[2],available[3]))
    print("P1\t{}\t{}\t{}\t{}\t\tP1\t{}\t{}\t{}\t{}\t\t".format(allocation[1][0],allocation[1][1],allocation[1][2],allocation[1][3],  
                                                                                    needed[1][0],needed[1][1],needed[1][2],needed[1][3]))
    print("P2\t{}\t{}\t{}\t{}\t\tP2\t{}\t{}\t{}\t{}\t\t".format(allocation[2][0],allocation[2][1],allocation[2][2],allocation[2][3],  
                                                                                    needed[2][0],needed[2][1],needed[2][2],needed[2][3]))                                                                                
    print("P3\t{}\t{}\t{}\t{}\t\tP3\t{}\t{}\t{}\t{}\t\t".format(allocation[3][0],allocation[3][1],allocation[3][2],allocation[3][3],  
                                                                                    needed[3][0],needed[3][1],needed[3][2],needed[3][3]))
    print("P4\t{}\t{}\t{}\t{}\t\tP4\t{}\t{}\t{}\t{}\t\t".format(allocation[4][0],allocation[4][1],allocation[4][2],allocation[4][3],  
                                                                                    needed[4][0],needed[4][1],needed[4][2],needed[4][3]))
    print()

processes = ['p0', 'p1', 'p2', 'p3', 'p4']
resources = ['G', 'N', 'U', 'M']
number_of_processes = len(processes)
number_of_resources = len(resources)
Sequence = np.zeros((number_of_processes,),dtype=int)
visited = np.zeros((number_of_processes,),dtype=int)
maximum = np.array([[0,2,1,0],
                    [1,6,5,2],
                    [2,3,6,6],
                    [0,6,5,2],
                    [0,6,5,6]])
allocation = np.array([[0,1,1,0],
                    [1,2,3,1],
                    [1,3,6,5],
                    [0,6,3,2],
                    [0,0,1,4]])

available = np.array([1,5,2,0])
needed = maximum - allocation
print_data()
count = 0
while( count < number_of_processes ):
    temp=0
    for i in range( number_of_processes ):
        if( visited[i] == 0 ):
            if(check(i)):
                print("-------------------------------------------------------------------------")
                Sequence[count]=i;
                count+=1
                visited[i]=1
                temp=1
                for j in range(number_of_resources):
                    available[j] += allocation[i][j] 
                    allocation[i][j] = 0
                    needed[i][j] = 0
                print_data()
    if(temp == 0):
        break


if(count < number_of_processes):
    print('status: unsafe')
else:
    print("status: safe")
    print("sequence: <",end="")
    for i in Sequence:
        print(' {} '.format(processes[i]), end='')
    print('>')
