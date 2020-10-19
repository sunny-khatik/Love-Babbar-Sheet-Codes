 def detectLoop(self):  #m1 floyd's cycle finding algo
        slow_p = self.head 
        fast_p = self.head 
        while(slow_p and fast_p and fast_p.next): 
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p: 
                return True
        retrun False    
            
 def hashing(self):
        s = set() 
         temp = self.head 
         while (temp): 
            if (temp in s): 
                return True
                s.add(temp) 
     
            temp = temp.next
          
     
         return False
   
   
