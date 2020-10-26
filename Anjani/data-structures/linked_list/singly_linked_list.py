#!/usr/bin/env python
# coding: utf-8

# In[19]:


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def create(self, llist):
        if llist.head:
            print('\n\nLinked list is already created!')
            return llist
        while True:
            print('Enter -1 to stop.')
            n = int(input('Enter the number you want to insert: '))
            if n == -1:
                break
            link_node = Node(n)
            if not llist.head:
                llist.head = link_node
                llist.tail = link_node
            else:
                llist.tail.next = link_node
                llist.tail = link_node
        return llist
    
    def display(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot display empty list!')
            return llist
        node = llist.head
        while node != None:
            print(node.data, end = " -> ")
            node = node.next
        print('X')
    
    def ins_beg(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot insert in empty list!')
            return llist
        n = int(input('Enter the number you want to insert at the beginning: '))
        link_node = Node(n)
        link_node.next = llist.head
        llist.head = link_node
        return llist
    
    def ins_end(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot insert in empty list!')
            return llist
        n = int(input('Enter the number you want to insert: '))
        link_node = Node(n)
        llist.tail.next = link_node
        llist.tail = link_node
        return llist
    
    def ins_after(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot insert in empty list!')
            return llist
        num = int(input('Enter the value after which you want to insert: '))
        node_check = llist.head
        flag = 0
        while node_check is not None:
            if node_check.data == num:
                flag = 1
                break
            node_check = node_check.next
        if flag == 0:
            print('\n\nThe number is not present in the list. Please try again!')
            return llist
        n = int(input('Enter the number you want to insert: '))
        link_node = Node(n)
        link_node.next = node_check.next
        node_check.next = link_node
        return llist
    
    def ins_before(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot insert in empty list!')
            return llist
        num = int(input('Enter the value before which you want to insert: '))
        node_check = llist.head
        if llist.head.data == num:
            n = int(input('Enter the number you want to insert: '))
            link_node = Node(n)
            link_node.next = llist.head
            llist.head = link_node
            return llist
        flag = 0
        while node_check is not None:
            if node_check.data == num:
                flag = 1
                break
            prev_node = node_check
            node_check = node_check.next
        if flag == 0:
            print('\n\nThe number is not present in the list. Please try again!')
            return llist
        n = int(input('Enter the number you want to insert: '))
        link_node = Node(n)
        link_node.next = prev_node.next
        prev_node.next = link_node
        return llist
    
    def ins_k(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot insert in empty list!')
            return llist
        k = int(input('Enter the position at which you want to insert the element: '))
        if k < 1:
            print('\n\nPlease enter a valid position, i.e., a value greater than 1.')
            return llist
        if k == 1:
            n = int(input('Enter the number you want to insert: '))
            link_node = Node(n)
            link_node.next = llist.head
            llist.head = link_node
            return llist
        len_check_node = llist.head
        count = 0
        while len_check_node is not None:
            len_check_node = len_check_node.next
            count += 1
        if k > count + 1:
            print('\n\nThe list is not that long! Provide a smaller place position.')
            return llist
        prev_node = llist.head
        i = 0
        while i != k - 2:
            i += 1
            prev_node = prev_node.next
        n = int(input('Enter the number you want to insert: '))
        link_node = Node(n)
        link_node.next = prev_node.next
        prev_node.next = link_node
        return llist
    
    def del_beg(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot delete from empty list!')
            return llist
        removed_node = llist.head
        llist.head = llist.head.next
        removed_node = None
        return llist
    
    def del_end(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot delete from empty list!')
            return llist
        removed_node = llist.head
        if llist.head.next == None:
            llist.head = None
            return llist
        while removed_node.next.next is not None:
            removed_node = removed_node.next
        removed_node.next = None
        return llist
    
    def del_val(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot delete from empty list!')
            return llist
        n = int(input('Enter the value you want to delete: '))
        removed_node = llist.head
        check_node = llist.head
        flag = 0
        if llist.head.data == n:
            removed_node = llist.head
            llist.head = llist.head.next
            removed_node = None
            return llist
        while removed_node.next is not None:
            if removed_node.data == n:
                flag = 1
                break
            check_node = removed_node
            removed_node = removed_node.next
        if removed_node.data == n:
            flag = 1
        if flag == 0:
            print('\n\nThe number is not in the list! Please try again!')
            return llist
        check_node.next = removed_node.next
        removed_node = None
        return llist
    
    def del_after(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot delete from empty list!')
            return llist
        n = int(input('Enter the value of the element after which you want to delete: '))
        check_node = llist.head
        while check_node is not None:
            if check_node.data == n:
                flag = 1
                break
            check_node = check_node.next
        if check_node.next is None:
            print('\n\nThere is no node after this value OR the value provided is not in the list. Please try again!')
            return llist
        removed_node = check_node.next
        check_node.next = removed_node.next
        removed_node = None
        return llist
    
    def del_before(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot delete from empty list!')
            return llist
        n = int(input('Enter the value of the element before which you want to delete: '))
        if llist.head.data == n:
            print('\n\nThere is no node before this value. Please try again!')
            return llist
        if llist.head.next.data == n:
            removed_node = llist.head
            llist.head = llist.head.next
            removed_node = None
            return llist
        check_node = llist.head
        removed_node = llist.head
        flag = 0
        while check_node.next is not None:
            if check_node.data == n:
                flag = 1
                break
            pre_removed_node = removed_node
            removed_node = check_node
            check_node = check_node.next
        if check_node.data == n:
            flag = 1
        if flag == 0:
            print('\n\nThe value given is not in the list. Please try again!')
            return llist
        pre_removed_node.next = check_node
        removed_node = None
        return llist
    
    def del_k(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot delete from empty list!')
            return llist
        n = int(input('Enter the position where you want to delete: '))
        if n == 1:
            removed_node = llist.head
            llist.head = llist.head.next
            removed_node = None
            return llist
        removed_node = llist.head
        i = 0
        while removed_node is not None:
            i += 1
            if i == n:
                break
            pre_removed_node = removed_node
            removed_node = removed_node.next
        if removed_node is None:
            print('\n\nThe list is not that long. Please try again!')
            return llist
        pre_removed_node.next = removed_node.next
        removed_node = None
        return llist
    
    def del_list(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot delete from empty list!')
            return llist
        while llist.head is not None:
            llist = llist.del_beg(llist)
        return llist
    
    def sort_list(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot sort an empty list!')
            return llist
        if llist.head.next is None:
            print('\n\nAlready Sorted!')
            return llist
        # to-dos: - Put uSort here instead of bubble sort
        while True:
            link_node = llist.head
            flag = 0
            while link_node.next is not None:
                if link_node.data > link_node.next.data:
                    swap_data = link_node.data
                    link_node.data = link_node.next.data
                    link_node.next.data = swap_data
                    flag = 1
                link_node = link_node.next
            if flag == 0:
                break
        return llist
    
    def reverse_list(self, llist):
        pass
    
    def count_nodes(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot count nodes in an empty list!')
            return llist
        link_node = llist.head
        count = 0
        while link_node is not None:
            count += 1
            link_node = link_node.next
        print('\n\nThe linked list has', count, 'nodes')
    
    def search_node(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot search for nodes in an empty list!')
            return llist
        n = int(input('Enter the number you want to search for: '))
        link_node = llist.head
        flag = 0
        while link_node is not None:
            if link_node.data == n:
                flag = 1
                break
            link_node = link_node.next
        if flag:
            print('\n\nFound!')
        else:
            print('\n\nNot Found!')
    
    def root_nth_node(self, llist):
        if not llist.head:
            print('\n\nList is empty, cannot search for nodes in an empty list!')
            return llist
        i = 1
        j = 1
        link_node = llist.head
        root_node = None
        while link_node is not None:
            if i == j * j:
                if root_node is None:
                    root_node = llist.head
                else:
                    root_node = root_node.next
                j += 1
            i += 1
            link_node = link_node.next
        
        print('\n\nThe root n-th node is', root_node.data)

if __name__=='__main__':
    llist = linked_list()
    while True:
        print('Enter -1 to exit.')
        print('1. Create a linked list.')
        print('2. Display a linked list.')
        print('3. Insert at the beginning of the linked list.')
        print('4. Insert at the end of the linked list.')
        print('5. Insert element after a particular value in the linked list.')
        print('6. Insert element before a particular value in the linked list.')
        print('7. Insert element at the k-th position in the linked list.')
        print('8. Delete from the beginning of the linked list.')
        print('9. Delete from the end of the linked list.')
        print('10. Delete user inputted elements from the linked list.')
        print('11. Delete after a particular value from the linked list.')
        print('12. Delete before a particular value from the linked list.')
        print('13. Delete at the k-th position from the linked list.')
        print('14. Delete the entire list.')
        print('15. Sort the entire list.')
        print('16. Reverse a list.')
        print('17. Count the number of nodes in a list.')
        print('18. Search for a number in the list.')
        print('19. Find the root n-th node in the list (in one scan).')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            llist = llist.create(llist)
        elif ch == 2:
            llist.display(llist)
        elif ch == 3:
            llist.ins_beg(llist)
        elif ch == 4:
            llist = llist.ins_end(llist)
        elif ch == 5:
            llist = llist.ins_after(llist)
        elif ch == 6:
            llist = llist.ins_before(llist)
        elif ch == 7:
            llist = llist.ins_k(llist)
        elif ch == 8:
            llist = llist.del_beg(llist)
        elif ch == 9:
            llist = llist.del_end(llist)
        elif ch == 10:
            llist = llist.del_val(llist)
        elif ch == 11:
            llist = llist.del_after(llist)
        elif ch == 12:
            llist = llist.del_before(llist)
        elif ch == 13:
            llist = llist.del_k(llist)
        elif ch == 14:
            llist = llist.del_list(llist)
        elif ch == 15:
            llist = llist.sort_list(llist)
        elif ch == 16:
            llist = llist.reverse_list(llist)
        elif ch == 17:
            llist.count_nodes(llist)
        elif ch == 18:
            llist.search_node(llist)
        elif ch == 19:
            llist.root_nth_node(llist)
        else:
            break


# In[ ]:




