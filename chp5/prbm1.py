class reverse_iter:
      def __init__(self,n):
          self.i = 0
          self.n = n
      def next(self):
          if self.i < self.n:
             x = self.n
             self.n -= 1
             return x
          else:
             raise StopIteration()

a = reverse_iter(5)
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()
print a.next()

