import unittest
import LoadDataset as LD
import matplotlib.image as misc
import numpy as np



class TestLoadData(unittest.TestCase):
    def setUp(self):
        pass

    def test_directory(self):
        load_data = LD.LoadData('/Users/mdabdulkadir/WS1819/ADAI/imagetest')
        # Example for retriving data.

        X ,Y = load_data.generate_data_2cls()
        # print ('Input dimention (X ): ', np.shape(X[0]) , ', Outputshape (Y) : ' , np.shape(Y)[0], 'Y values : ' , Y )
        # self.assertEqual(Y, [0 , 1])
        self.assertEqual(X[0][100,69,2],misc.imread('/Users/mdabdulkadir/WS1819/ADAI/imagetest/c0/Unknown.png')[100,69,2])
        # self.assertEqual(2,2)



if __name__ == '__main__':
    unittest.main()
