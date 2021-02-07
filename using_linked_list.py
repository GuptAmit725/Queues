class node:
	def __init__(self, info, next=None):
		self.info = info
		self.next = next

class Queue:
	def __init__(self):
		self.front = None
		self.rear = None		

	def isEmpty(self):
		return self.front == None

	def EnQueue(self,ele):
		temp = node(ele)
		if self.rear == None:
		 	self.rear = self.front = temp
           # return
		self.rear.next = temp
		self.rear = temp

	def DeQueue(self):
		if self.isEmpty():
			print('Queue is emppty!')
            #return
		temp = self.front 
		self.front = temp.next
		if self.front == None:
			self.rear = None

	def display(self):
		p = self.front
		while p != None:
			print(p.info)
			p = p.next	
q = Queue()
q.EnQueue(10)			
q.EnQueue(20)			
q.EnQueue(30)
print()
q.display()
q.DeQueue()	
print('********')
q.display()		
