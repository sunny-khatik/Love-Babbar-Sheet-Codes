# https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1
def segregate(self, head):
        end = head
        c0,c1,c2=0,0,0
        while end != None:
            gotu = end.data
            if gotu == 0:
                c0+=1
            elif gotu == 1:
                c1+=1
            else:
                c2+=1
            end=end.next
        end=head
        while end != None:
            if c0:
                end.data=0
                c0-=1
            elif c1:
                end.data=1
                c1-=1
            else:
                end.data=2
                c2-=1
            end=end.next
        return head
