#!/usr/bin/env python
# -*- coding: utf-8 -*-

#��O��1����ʱ����ɾ���ڵ�
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
		# ���Դ�ӡ��
		while(pHead != None):
			print pHead.val
			pHead=pHead.next

	def midoflist(self,pHead):
		fast,slow = pHead,pHead
		while fast and fast.next: 
		#�����������Ҫ���������Ϊfast.next�Ļ������Nonetypeû��next�������
		#fast ��ǰ�����fast�Ѿ�ΪNone����ô��fast.nextҲһ��������	
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
		#һ�������һ���ڵ�ָ����һ����ͷ
		#�ж��Ƿ��л�
		#�ڶ��ַ������ж�������������һ���ڵ��Ƿ���ͬ
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
	# ���һ�������л�������ж����������ཻ�����ϵĽڵ�ͬʱ����������
	# # �ཻ�ĵ�һ���ڵ�


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


# ����жϵĲ��ԣ������ֻ��һ���ڵ���ɾ��������Ϊ��
# �������ܶ���ڵ㣬��ɾ�����һ��ͷ�ڵ����Ļ������

'''
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # ����ListNode
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