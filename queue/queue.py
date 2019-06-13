class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage =  []

#Should insert into the back of the queue.
  def enqueue(self, item):
    self.storage.insert(0, item)
  
  #Should remove and return from the front of the queue
  def dequeue(self):
    if len(self.storage) > 0:
      return self.storage.pop()

#Should return the number of items in the queue.
  def len(self):
    return  len(self.storage)
