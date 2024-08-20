#User function Template for python3

# class Solution:
#     #Complete this function
#     def power(self,N,R):
#         #Your code here
#         mod = 1000000007
#         if R == 0:
#             return 1
#         if R % 2 == 0:
#             half_power = self.power(N, R // 2)
#             return (half_power * half_power) % mod
#         else:
#             return (N * self.power(N, R - 1)) % mod

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        return int(pow(N,R,1000000007))
    
import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-= 1

if __name__ == "__main":
    main()
