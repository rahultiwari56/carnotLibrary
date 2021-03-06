import os
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

'''
    Incase if any issue with pandas or xlrd, please run the below commannds,
    since latest version of pandas have bugs as per the issue raised in their 
    official repo
'''
# !pip install --upgrade openpyxl 
# # !pip install xlrd==1.2.0

load_dotenv()

# db credentials
dbuser = os.getenv('DBUSER')
dbpassword = os.getenv('DBPASSWORD')
dbname = os.getenv('DBNAME')
dbhost = os.getenv('DBHOST')

def eda(file_name):
    '''
        Description: This function is used for data pre-processing and transformation
        Input: Takes input as a excel file path
        Output: Returns pre-processed and transformed data
    '''

    # read file
    student = pd.read_excel(file_name, 'Students')
    school = pd.read_excel(file_name, 'Schools')
    book = pd.read_excel(file_name, 'Books')

    # filling null
    student['gender'].replace(np.nan, 'Prefer not to say', inplace=True)

    # mapping the id of book table to the student table
    dummpy_data = [data for data in book['Title']]
    student['book_id'] = student['books'].apply(lambda x : dummpy_data.index(x) if x in dummpy_data else np.nan)
    # dropping the book column
    student.drop(columns=['books'], inplace=True)

    # mapping the id of school table to the student table
    dummpy_data = [data for data in school['school']]
    student['school_id'] = student['school'].apply(lambda x : dummpy_data.index(x) if x in dummpy_data else np.nan)
    student['book_id'] = student['book_id']+1
    student['school_id'] = student['school_id']+1
    student['school_id'] = student['school_id'].astype(pd.Int32Dtype()) # converting to int from float
    student['book_id'] = student['book_id'].astype(pd.Int32Dtype())

    student.drop(columns=['school'], inplace=True)

    # renaming the columns
    school.rename(columns = {'REGIONID':'region_id', 'school_id':'id', 'address2':'address'}, inplace = True)
    student.rename(columns = {'ID':'id'}, inplace = True)
    book.rename(columns = {'book_id':'id','Author Name':'Author_Name', 'Date of Publication':'Date_Of_Publication', 'Number of Pages': 'Number_Of_Pages'}, inplace = True)

    return student, school, book



def insert_to_db(table_data):
    '''
        This function add data from the dataframe to the respective database.
        Input: Dictionary containing Dataframes
        Output: Inserts datas to the tables School, Book and Student

        
    '''
    try:
        engine = create_engine(f'postgresql://{dbuser}:{dbpassword}@{dbhost}/{dbname}', echo=False)
        conn = engine.connect().connection

        for table_name, table_values in table_data.items():
            table_values.to_sql("library_"+table_name, con=engine, schema=None, index=False, if_exists='append', method="multi")

        conn.close()

        return "Data Inserted Successfully."
    except:
        return "Data Insertion Failed."



if __name__=='__main__':
    file_name = 'Data.xls'
    # data preprocessing
    student, school, book = eda(file_name)

    # print(student)

    insert_to_db({"school": school, "book": book, "student": student})
