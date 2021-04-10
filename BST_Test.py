import unittest
from Binary_Search_Tree import Binary_Search_Tree

class BST_Test(unittest.TestCase):
   
   def setUp(self):
      self.__bst = Binary_Search_Tree()
      
   
   #_________RAISING ERRORS TEST CASES_____________
      
   #tests if value error is raised when value the same as the root is inserted    
   def test_insert_same_root_value_ignore(self):
      self.__bst.insert_element(1)
      with self.assertRaises(ValueError):
         self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', str(self.__bst))
      
   #tests if value error is raised when value the same as a leaf node is inserted  
   def test_insert_same_leaf_value_ignore(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      with self.assertRaises(ValueError):
         self.__bst.insert_element(1)
      self.assertEqual('[ 1, 2, 3 ]', str(self.__bst))
    
   #tests if value error is raised when value is removed from an empty binary search tree  
   def test_remove_empty_bst_ignore(self):
      with self.assertRaises(ValueError):
         self.__bst.remove_element(1)
      self.assertEqual('[ ]', str(self.__bst))
      
   #tests if value error is raised when value is removed that does not exist in a binary search tree with values in it 
   def test_remove_bst_ignore(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(1)
      self.__bst.insert_element(2)
      with self.assertRaises(ValueError):
         self.__bst.remove_element(3)
      self.assertEqual('[ 1, 2, 4 ]', str(self.__bst))
          
   #_________INSERTION TEST CASES (INORDER)_____________
   
   #tests in order traversal of an empty binary search tree
   def test_empty_bst_inorder(self):
      self.assertEqual('[ ]', self.__bst.in_order())
   
   #tests in order traversal of a binary search tree after 1 value has been inserted into it   
   def test_insert_1_bst_inorder(self):
      self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree after 3 values have been inserted into it   
   def test_insert_3_bst_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual('[ 1, 2, 3 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree after 7 values have been inserted into it   
   def test_insert_7_bst_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(5)
      self.__bst.insert_element(7)
      self.assertEqual('[ 1, 2, 3, 4, 5, 6, 7 ]', self.__bst.in_order())
      
         
   #_________INSERTION TEST CASES (PREORDER)_____________
   
   #tests pre order traversal of an empty binary search tree
   def test_empty_bst_preorder(self):
      self.assertEqual('[ ]', self.__bst.pre_order())
   
   #tests pre order traversal of a binary search tree after 1 value has been inserted into it   
   def test_insert_1_bst_preorder(self):
      self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree after 3 values have been inserted into it   
   def test_insert_3_bst_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual('[ 2, 1, 3 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree after 7 values have been inserted into it   
   def test_insert_7_bst_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(5)
      self.__bst.insert_element(7)
      self.assertEqual('[ 4, 2, 1, 3, 6, 5, 7 ]', self.__bst.pre_order())
   
   
   
   #_________INSERTION TEST CASES (POSTORDER)_____________
   
   #tests post order traversal of an empty binary search tree
   def test_empty_bst_postorder(self):
      self.assertEqual('[ ]', self.__bst.post_order())
   
   #tests post order traversal of a binary search tree after 1 value has been inserted into it   
   def test_insert_1_bst_postorder(self):
      self.__bst.insert_element(1)
      self.assertEqual('[ 1 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree after 3 values have been inserted into it   
   def test_insert_3_bst_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual('[ 1, 3, 2 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree after 7 values have been inserted into it   
   def test_insert_7_bst_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.insert_element(5)
      self.__bst.insert_element(7)
      self.assertEqual('[ 1, 3, 2, 5, 7, 6, 4 ]', self.__bst.post_order())
      
      
    
   #_________GET HEIGHT TEST CASES_____________
    
   #tests height of an empty binary search tree
   def test_empty_bst_height(self):
      self.assertEqual(0, self.__bst.get_height())
      
   #tests height of a binary search tree with 1 value inserted into it
   def test_insert_1_bst_height(self):
      self.__bst.insert_element(1)
      self.assertEqual(1, self.__bst.get_height())
      
   #tests height of a binary search tree with 3 values inserted into it on the left side
   def test_insert_3_bst_left_height(self):
      self.__bst.insert_element(3)
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.assertEqual(3, self.__bst.get_height())
   
   #tests height of a binary search tree with 3 values inserted into it on the right side
   def test_insert_3_bst_right_height(self):
      self.__bst.insert_element(1)
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.assertEqual(3, self.__bst.get_height())
      
   #tests height of a binary search tree with 3 values inserted into it 
   def test_insert_3_bst_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual(2, self.__bst.get_height())
      
   #tests height of a binary search tree with 5 values inserted into it 
   def test_insert_5_bst_height(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.assertEqual(3, self.__bst.get_height())
      
   #tests height of a binary search tree after removing a node with no children   
   def test_0_children_bst_remove_height(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual(0, self.__bst.get_height())
      
   #tests height of a binary search after removing a node with 1 child on its left
   def test_1_left_child_bst_remove_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual(1, self.__bst.get_height())
      
   #tests height of a binary search after removing a node with 1 child on its right
   def test_1_right_child_bst_remove_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual(1, self.__bst.get_height())
      
   #tests height of a binary search after removing a node with 2 children
   def test_2_children_bst_remove_height(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual(2, self.__bst.get_height())
      
   
   #_________REMOVE TEST CASES (INORDER)_____________
   
   #tests in order traversal of a binary search tree that has its root value removed when it has no children   
   def test_0_children_bst_remove_root_inorder(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has its root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_root_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has its root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_root_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has its root value removed when it has 2 children  
   def test_2_children_bst_remove_root_inorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has no children   
   def test_0_children_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 4, 6 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 4, 6 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.__bst.remove_element(6)
      self.assertEqual('[ 2, 4, 7 ]', self.__bst.in_order())
      
   #tests in order traversal of a binary search tree that has a non-root value removed when it has 2 children  
   def test_2_children_bst_remove_nonroot_inorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3, 4, 6 ]', self.__bst.in_order())
      
      
      
   #_________REMOVE TEST CASES (PREORDER)_____________
   
   #tests pre order traversal of a binary search tree that has its root value removed when it has no children   
   def test_0_children_bst_remove_root_preorder(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has its root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_root_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has its root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_root_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has its root value removed when it has 2 children  
   def test_2_children_bst_remove__root_preorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3, 1 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has no children   
   def test_0_children_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ 4, 2, 6 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 4, 1, 6 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.__bst.remove_element(6)
      self.assertEqual('[ 4, 2, 7 ]', self.__bst.pre_order())
      
   #tests pre order traversal of a binary search tree that has a non-root value removed when it has 2 children  
   def test_2_children_bst_remove_nonroot_preorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 4, 3, 1, 6 ]', self.__bst.pre_order())
      
      
      
   #_________REMOVE TEST CASES (POSTORDER)_____________
   
   #tests pre order traversal of a binary search tree that has its root value removed when it has no children   
   def test_0_children_bst_remove_root_postorder(self):
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has its root value removed when it has 1 child on its left
   def test_1_left_child_order_bst_remove_root_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has its root value removed when it has 1 child on its right
   def test_1_right_child_order_bst_remove_root_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 3 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has its root value removed when it has 2 children  
   def test_2_children_bst_remove_root_postorder(self):
      self.__bst.insert_element(2)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has no children   
   def test_0_children_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(1)
      self.assertEqual('[ 2, 6, 4 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has 1 child on its left
   def test_1_left_child_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 6, 4 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has 1 child on its right
   def test_1_right_child_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(7)
      self.__bst.remove_element(6)
      self.assertEqual('[ 2, 7, 4 ]', self.__bst.post_order())
      
   #tests post order traversal of a binary search tree that has a non-root value removed when it has 2 children  
   def test_2_children_bst_remove_nonroot_postorder(self):
      self.__bst.insert_element(4)
      self.__bst.insert_element(2)
      self.__bst.insert_element(6)
      self.__bst.insert_element(1)
      self.__bst.insert_element(3)
      self.__bst.remove_element(2)
      self.assertEqual('[ 1, 3, 6, 4 ]', self.__bst.post_order())
           
if __name__ == '__main__':
   unittest.main()
