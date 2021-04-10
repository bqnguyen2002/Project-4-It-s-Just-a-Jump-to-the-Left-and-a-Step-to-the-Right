class Binary_Search_Tree:
   # TODO.I have provided the public method skeletons. You will need
   # to add private methods to support the recursive algorithms
   # discussed in class

   
   #recursively updates the height of the tree
   def update_height(self, node):
      if node is None: 
         return 0
      else:
         return 1 + max(self.update_height(node.left), self.update_height(node.right))
                
   #recursively inserts a new node with a value of 'val' into the tree    
   def __rec_insert_element(self, node, val):
      if node is None:  
         return Binary_Search_Tree.__BST_Node(val)
             
      if node.value == val: 
         raise ValueError
          
      if val < node.value:
         node.left = self.__rec_insert_element(node.left, val)
      else: 
         node.right = self.__rec_insert_element(node.right, val) 
           
      node.height = self.update_height(node)        
      return node
        
   #finds the minimum value in a sub tree
   def minVal(self, node):
      current = node
      while current.left is not None:
         current = current.left
      return current.value
           
   #recursively removes a node with a value of 'val' from the tree   
   def __rec_remove_element(self, node, val):
      if node is None: 
         raise ValueError
         
      if val == node.value: #2 children
         if node.left is None and node.right is None:
            return None
         elif node.left is None: #1 child on its right
            return node.right
         elif node.right is None: #1 child in its left
            return node.left
         else: #no children
            node.value = self.minVal(node.right)
            node.right = self.__rec_remove_element(node.right, node.value)    
      
      elif val < node.value: 
         node.left = self.__rec_remove_element(node.left, val)
      elif val > node.value:
         node.right = self.__rec_remove_element(node.right, val)
            
      node.height = self.update_height(node)
      return node     
      
   #returns in order traversal of tree as a string               
   def __rec_in_order(self, root, string):
      string = ''
      if root is not None:
         string += self.__rec_in_order(root.left, string)
         string += str(root.value) + ', '
         string += self.__rec_in_order(root.right, string)
      return string
      
   #returns pre order traversal of tree as a string
   def __rec_pre_order(self, root, string):
      string = ''
      if root is not None:
         string += str(root.value) + ', '
         string += self.__rec_pre_order(root.left, string)
         string += self.__rec_pre_order(root.right, string)
      return string
      
   #returns post order traversal of tree as a string
   def __rec_post_order(self, root, string):
      string = ''
      if root is not None:
         string += self.__rec_post_order(root.left, string)
         string += self.__rec_post_order(root.right, string)
         string += str(root.value) + ', '
      return string
        
   class __BST_Node:
      # TODO The Node class is private. You may add any attributes and
      # methods you need. Recall that attributes in an inner class 
      # must be public to be reachable from the the methods.
   
      def __init__(self, value):
         self.value = value
         self.left = None
         self.right = None
         self.height = 1
       # TODO complete Node initialization

   def __init__(self):
      self.__root = None
     # TODO complete initialization

   def insert_element(self, value):
      self.__root = self.__rec_insert_element(self.__root, value)
      # Insert the value specified into the tree at the correct
      # location based on "less is left; greater is right" binary
      # search tree ordering. If the value is already contained in
      # the tree, raise a ValueError. Your solution must be recursive.
      # This will involve the introduction of additional private
      # methods to support the recursion control variable.
      # TODO replace pass with your implementation

   def remove_element(self, value):
      self.__root = self.__rec_remove_element(self.__root, value)
      # Remove the value specified from the tree, raising a ValueError
      # if the value isn't found. When a replacement value is necessary,
      # select the minimum value to the from the right as this element's
      # replacement. Take note of when to move a node reference and when
      # to replace the value in a node instead. It is not necessary to
      # return the value (though it would reasonable to do so in some 
      # implementations). Your solution must be recursive. 
      # This will involve the introduction of additional private
      # methods to support the recursion control variable.
      # TODO replace pass with your implementation

   def in_order(self):
      inorderString = ''
      if self.__root is None:
         return '[ ]'
      else:
         result = self.__rec_in_order(self.__root, inorderString)
         return '[ ' + result[0: len(result)-2] + ' ]' 
      # Construct and return a string representing the in-order
      # traversal of the tree. Empty trees should be printed as [ ].
      # Trees with one value should be printed as [ 4 ]. Trees with more
      # than one value should be printed as [ 4, 7 ]. Note the spacing.
      # Your solution must be recursive. This will involve the introduction
      # of additional private methods to support the recursion control 
      # variable.
      # TODO replace pass with your implementation
      

   def pre_order(self):
      preorderString = ''
      if self.__root is None:
         return '[ ]'
      else:
         result = self.__rec_pre_order(self.__root, preorderString)
         return '[ ' + result[0: len(result)-2] + ' ]' 
      # Construct and return a string representing the pre-order
      # traversal of the tree. Empty trees should be printed as [ ].
      # Trees with one value should be printed in as [ 4 ]. Trees with
      # more than one value should be printed as [ 4, 7 ]. Note the spacing.
      # Your solution must be recursive. This will involve the introduction
      # of additional private methods to support the recursion control 
      # variable.
      # TODO replace pass with your implementation

   def post_order(self):
      postorderString = ''
      if self.__root is None:
         return '[ ]'
      else:
         result = self.__rec_post_order(self.__root, postorderString)
         return '[ ' + result[0: len(result)-2] + ' ]' 
      # Construct an return a string representing the post-order
      # traversal of the tree. Empty trees should be printed as [ ].
      # Trees with one value should be printed in as [ 4 ]. Trees with
      # more than one value should be printed as [ 4, 7 ]. Note the spacing.
      # Your solution must be recursive. This will involve the introduction
      # of additional private methods to support the recursion control 
      # variable.
      # TODO replace pass with your implementation

   def get_height(self):
      if self.__root is None:
         return 0
      return self.__root.height 
      # return an integer that represents the height of the tree.
      # assume that an empty tree has height 0 and a tree with one
      # node has height 1. This method must operate in constant time.
      # TODO replace pass with your implementation

   def __str__(self):
      return self.in_order()

#if __name__ == '__main__':
#pass

   
 



   
