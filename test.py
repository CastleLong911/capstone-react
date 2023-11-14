import sys
sys.setrecursionlimit(10**7)

def electricity(pp, cp, wires, cutted):
    count = 0
    for i in wires:
        if (i[0] == cp or i[1] == cp) and (i[0] != pp or i[1] != pp):
            count += 1 + electricity(cp, i[0] if i[0] != cp else i[1], wires, cutted)
    return count        
    
def solution(n, wires):
    answer = -1
    
    for i in wires:
        a = electricity(0, i[0], wires, i)
        b = electricity(0, i[1], wires, i)
        
            
    
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])