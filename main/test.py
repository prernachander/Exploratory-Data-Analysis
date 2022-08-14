import lib.FeatureEngineering as fe
import lib.stats as st
import lib.viz as vz
import unittest

class test(unittest.TestCase):
    
    def test_data_cleanup(self):
        """
        Testing the data_cleanup() function by using the fail test scenario for file types
        """
        df = fe.data('data/test.txt')
        self.assertRaises(ValueError, df.data_cleanup,'txt')
        
    def test_data_engineering(self):
        """
        Testing the data_engineering() function by using the fail test scenario for non pandas dataframe input
        """
        df = fe.data('data/test.txt')
        self.assertRaises(ValueError, df.data_engineering)
        
    def test_split_train_test(self):
        """
        Testing split_train_test() function by matching the number of rows of the train & test DataFrames
        (70/30 split)
        """
        x = st.stats('data/iris.csv')
        out_train, out_test = x.split_train_test()
        self.assertEqual(len(out_train), 105)
        self.assertEqual(len(out_test), 45)

    def test_median(self):
        """
        Testing median() function by checking the output of some numerical lists
        """
        out = st.stats().median([2, 2, 4, 6, 8])
        self.assertEqual(out, 4)
        out2 = st.stats().median([1, 7, 3, 5, 3, 9])
        self.assertEqual(out2, 4)
        out3 = st.stats().median([1, 2, 1, 3, 4, 2])
        self.assertEqual(out3, 2)
        
    def test_mean(self):
        """
        Testing mean() function by checking the output of some numerical lists
        """
        out = st.stats().mean([2, 2, 4, 6, 8])
        self.assertEqual(out, 4.4)
        out2 = st.stats().mean([1, 3, 3, 5, 7, 8])
        self.assertEqual(out2, 4.5)
        out3 = st.stats().mean([1, 1, 2, 2, 3, 9])
        self.assertEqual(out3, 3)
        
    def test_calc_quartiles(self):
        """
        Testing calc_quartiles() function by checking the output of some numerical lists
        """
        out_q1, out_q3 = st.stats().calc_quartiles([20, 30, 50, 60, 70, 90])
        self.assertEqual(out_q1, 30)
        self.assertEqual(out_q3, 70)
        out2_q1, out2_q3 = st.stats().calc_quartiles([1, 5, 6, 7, 8, 9, 10])
        self.assertEqual(out2_q1, 5.5)
        self.assertEqual(out2_q3, 8.5)
    
    def test_select_options(self):
        df = vz.viz('data/iris.csv')
        try:
            df.select_options(df)
        except:
            self.fail()
        

if __name__ == '__main__':
    unittest.main()