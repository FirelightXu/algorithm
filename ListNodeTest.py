#!/usr/bin/env python
# -*- coding: utf-8 -*-

#在O（1）的时间内删除节点
class ListNode():
	def __init__(self,num):
		self.val = num
		self.next = None

class solution:
	def deleteNode(self,pHead,Node):
		if Node == None or pHead == None:
			return
		if Node.next != None:
			Node.val = Node.next.val
			Node.next = Node.next.next
		elif Node == pHead:
			pHead = None
			pHead.val = None
			pHead.next = None

		else:
			pNode = pHead
			while pNode.next != Node:
				pNode = pNode.next
			pNode.next = None
		
		# return pHead
		# 测试打印用
		while(pHead != None):
			print pHead.val
			pHead=pHead.next

	def midoflist(self,pHead):
		fast,slow = pHead,pHead
		while fast and fast.next: 
		#这个条件很重要，如果设置为fast.next的话会出现Nonetype没有next这个错误。
		#fast 在前，如果fast已经为None，那么，fast.next也一定不存在	
			fast=fast.next.next
			slow=slow.next
		print slow.val
	def cricle(self,pHead):
		fast,slow = pHead,pHead
		while fast and fast.next:
			fast=fast.next.next
			slow = slow.next
			if (fast == slow):
				print "youhuan"
				return
		print "meiyou"
		return
	def xiangjiao(self,pHead1,pHead2):
		pass
		#一个的最后一个节点指向另一个的头
		#判断是否有环
		#第二种方法是判断两个链表的最后一个节点是否相同
	def circlestart(self,pHead):
		fast,slow = pHead,pHead
		while fast and fast.next:
			fast = fast.next.next
			slow = slow.next
			if (fast == slow):
				break
		slow = pHead
		while fast !=slow:
			fast=fast.next
			slow=slow.next
		print fast.val
		return fast
	# 如果一个链表有环，如何判断两个链表相交：则环上的节点同时在两个链表
	# # 相交的第一个节点


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3		

s = solution()
# s.deleteNode(node1,node1)
s.circlestart(node1)


# 这个判断的策略，如果是只有一个节点则删除完链表为空
# 如果链表很多个节点，则删除完第一个头节点后面的还能输出

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pnode = pHead
        preverseHead = None
        ppre = None
        while pnode!= None:
            pnext = pnode.next
            if pnext == None:
                preverseHead = pnode
            pnode.next=ppre
            ppre=pnode
            pnode = pnext
        return preverseHead
        # write code here
'''