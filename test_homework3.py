import unittest
import sys
import homework3 as hw

# Define a class that tests the module homework3
class TestHomework(unittest.TestCase):
    #Check if path variable was passed
    try:
        sys.argv[1]
    except (IndexError):
        INPUT_PATH = 'class.db'
    else:
        if(sys.argv[1] == '-f'): #handle jupyter notebook default
            INPUT_PATH = 'class.db'
        else:
            INPUT_PATH = sys.argv[1]
    
    #Check if ValueError message is shown for fakepath
    def test_ValueErrorWithBadPath(self):
        fake_path = 'fakepath..'
        with self.assertRaises(ValueError):
            outFrame = hw.create_dataframe(fake_path)
    
     #Check if there at least 10 rows in inputFrame
    def test_Atleast10Rows(self):
        df = hw.create_dataframe(self.INPUT_PATH)
        frameLen = len(df)
        rowCheck = (frameLen >= 10)
        self.assertTrue(rowCheck)
    
    #Check if inputFrame columns are expected columns
    def test_ExpectedColumns(self):
        df = hw.create_dataframe(self.INPUT_PATH)
        expectedCols = ['video_id','language','category_id']
        expectedCols.sort()
        inputCols = df.columns.tolist()
        inputCols.sort()
        columnCheck = inputCols == expectedCols
        self.assertTrue(columnCheck)

    #Check that video_id and language are key
    def test_ColsAreKey(self):
        df = hw.create_dataframe(self.INPUT_PATH)
        frameLen = len(df)
        keyCols = ['video_id', 'category_id']
        keyLength = len(df[keyCols].drop_duplicates())
        keyCheck = (frameLen == keyLength)
        self.assertTrue(keyCheck)

if __name__ == '__main__':
    unittest.main()
