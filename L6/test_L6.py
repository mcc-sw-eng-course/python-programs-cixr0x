import unittest
import L6
import filecmp
import os

class TestFirstExercises(unittest.TestCase):
    
    def test_setinputdata(self):
        listOfData=[55.0, 20.0, 32.0, 15.0, 1.0, 100.0, 20.0, 99.0, 7.0, 5.0, 3.0, 6.0, 7.0, 1.0, 0.5, 4.0, 1.0]
        srtDt=L6.DataSorter()
        srtDt.set_input_data('Book1.csv')
        self.assertEqual(srtDt.lst, listOfData)
        
        
        with self.assertRaises(FileNotFoundError):
            srtDt.set_input_data('Book3.csv')

        with self.assertRaises(ValueError):
            srtDt.set_input_data('Book2.csv')
    
    def test_mergeSort(self):
        orderedData=[0.5, 1.0, 1.0, 1.0, 3.0, 4.0, 5.0, 6.0, 7.0, 7.0, 15.0, 20.0, 20.0, 32.0, 55.0, 99.0, 100.0]
        srtDt=L6.DataSorter()
        srtDt.set_input_data('Book1.csv')
        srtDt.set_output_data('Book1Sorted.csv')
        srtDt.execute_merge_sort()
        
        self.assertEqual(srtDt.lst, orderedData)
    
    def test_set_output_data(self):
         srtDt=L6.DataSorter()
         srtDt.set_input_data('Book1.csv')
         srtDt.set_output_data("SortedBook2.csv")
         srtDt.execute_merge_sort()         
         self.assertTrue(filecmp.cmp("SortedBook2.csv","Book1Sorted.csv"))
         os.remove("SortedBook2.csv") 
        
        
if __name__ == '__main__':
    unittest.main()