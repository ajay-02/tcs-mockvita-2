def minPartition(S):
    total=sum(S)
    T=[[False]*(total+1) for _ in range(len(S)+1)]
    for i in range(len(S)+1):
        T[i][0]=True
        j=1
        while i > 0 and j <= total:
            T[i][j]=T[i-1][j]
            if S[i-1] <= j:
                T[i][j]|=T[i-1][j-S[i-1]]
                j = j + 1
    j=total//2
    while j >= 0 and not T[len(S)][j]:
        j = j - 1
    print(total-j)
    return total - 2 * j
if __name__ == '__main__':
    S = [25,30,35,20,90,110,45,70,80,12,30,35,85]
    print("The minimum difference is", minPartition(S))
