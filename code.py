class Solution:
     def strongPasswordChecker(self, password):
        ans = 0 if any([password[i].isdigit() for i in range(len(password))]) else 1
        ans += 0 if any([password[i].islower() for i in range(len(password))]) else 1
        ans += 0 if any([password[i].isupper() for i in range(len(password))]) else 1

        if len(password) <  6:  return max(6 - len(password), ans)   

        g = [len(list(g)) for _, g in groupby(password)]
        g = [r for r in g if r > 2]

        if len(password) > 20:                                  
            g = [(r%3, r) for r in g]
            heapify(g)
            for i in range(len(password)-20): 
                if not g: break
                _, r = heappop(g)
                if r > 3: heappush(g, ((r-1)%3, r-1))
            g = [r for _,r in g]
 
        return max(ans, sum(r//3 for r in g))+max(0,len(password)-20)  
'''
Time complexity:
O(n)

Space complexity:
O(1)
'''
 

        


