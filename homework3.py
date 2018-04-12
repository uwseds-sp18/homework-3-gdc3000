#import packages
import sqlite3
import pandas as pd
import os

#Question 1: Create function which creates dataframe by running query against class db file at given path.
def create_dataframe(dbPath):
    if not os.path.isfile(dbPath):
        raise ValueError("Path '{0}' is incorrect.".format(dbPath))     
    #Query that will be run
    query = """
            SELECT DISTINCT video_id, category_id, 'ca' as language FROM CAvideos
            UNION ALL
            SELECT DISTINCT video_id, category_id, 'us' as language FROM USvideos
            UNION ALL
            SELECT DISTINCT video_id, category_id, 'gb' as language FROM GBvideos
            UNION ALL
            SELECT DISTINCT video_id, category_id, 'de' as language FROM DEvideos
            UNION ALL
            SELECT DISTINCT video_id, category_id, 'fr' as language FROM FRvideos;
            """
    conn = sqlite3.connect(dbPath)
    cur = conn.cursor()   
    return pd.read_sql_query(query, conn)

#Question 2: create function to test dataframe.
def test_create_dataframe(inputFrame):
    printDebug = False
    
    #Make sure input is dataframe. If not, throw exception.
    if not isinstance(inputFrame, pd.core.frame.DataFrame):
        raise ValueError("Input must be a pandas dataframe")
    
    #Check if there are at least 10 rows in inputFrame
    frameLen = len(inputFrame)
    rowCheck = frameLen >= 10
    if(printDebug):
        print('rowCheck:', rowCheck)
    
    #Check if inputFrame columns are expected columns
    expectedCols=['video_id','language','category_id']
    columnCheck = True
    for i in range(0,len(inputFrame.columns)):
        columnCheck = inputFrame.columns[i] in expectedCols
        if(printDebug):
            print('columnCheck, ',i,': ',columnCheck)
        if(not columnCheck):
            break

    #Check if video_id and language are a key
    keyCols = ['video_id', 'category_id']
    keyLength = len(df[keyCols].drop_duplicates())
    keyCheck = frameLen == keyLength
    if(printDebug):
        print('keylength: ',keyLength
              ,', frameLen: ',frameLen
              ,', keycheck:', keyCheck)
    
    #Return false if any of the checks are false	 
    return columnCheck and rowCheck and keyCheck
