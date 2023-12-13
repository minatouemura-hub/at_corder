def main():
    N = int(input())
    H = list(map(int,input().split()))
    #最小問題なのでinfに設定
    table = [float("inf")]*N
    
    table[0] = 0

    def chmin(a,b):
        if (a>b):
            return b
        return a
    
    for i in range(N):
        table[i] = chmin(table[i],table[i-1]+abs(H[i]-H[i-1]))
        if i >1:
            table[i] = chmin(table[i],table[i-2]+abs(H[i]-H[i-2]))
        
    print(table[N-1])
        

    
if __name__ == "__main__":
    main()