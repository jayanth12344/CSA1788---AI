class Tree_Struct:
   def __init__(self, key=None):
      self.key = key
      self.children = []

   def add_elem(self, node):
      self.children.append(node)
 
   def search_elem(self, key):
      if self.key == key:
         return self
      for child in self.children:
         temp = child.search_elem(key)
         if temp is not None:
            return temp
      return None

   def postorder_traversal(self):
      for child in self.children:
         child.postorder_traversal()
      print(self.key, end=' ')

my_instance = None

print('Menu (this assumes no duplicate keys)')
print('add <data> at root')
print('add <data> below <data>')
print('dfs')
print('quit')

while True:
   my_input = input('What operation would you do ? ').split()

   operation = my_input[0].strip().lower()
   if operation == 'add':
      data = int(my_input[1])
      new_node = Tree_Struct(data)
      suboperation = my_input[2].strip().lower()
      if suboperation == 'at':
         my_instance = new_node
      else:
         position = my_input[3].strip().lower()
         key = int(position)
         ref_node = None
         if my_instance is not None:
            ref_node = my_instance.search_elem(key)
         if ref_node is None:
            print('No such key exists')
            continue
         ref_node.add_elem(new_node)

   elif operation == 'dfs':
      print('The post-order traversal is : ', end='')
      my_instance.postorder_traversal()
      print()

   elif operation == 'quit':
      break
