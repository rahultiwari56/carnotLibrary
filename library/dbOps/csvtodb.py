import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pandas.io.sql as psql



def eda(file_name):

    # read file
    df = pd.read_excel(file_name)

    # df.head()

    df = df.fillna('')

    # generating unique id's
    df['school_id'] = pd.factorize(df['school'])[0]
    df['book_id'] = pd.factorize(df['books'])[0]

    # remove id of null values
    # df.loc[df["book_id"] == 2, "book_id"] = ''
    # df.loc[df["school_id"] == 12, "school_id"] = ''

    # replacing id of empty value with NaN
    df['school_id'].replace(12, np.nan, inplace=True)
    df['book_id'].replace(2, np.nan, inplace=True)

    # fill null values (gender column)
    df['gender'].replace('', 'Prefer not to say', inplace=True)

    # splitting students column
    student = df[['ID', 'first_name', 'last_name', 'email', 'gender', 'school_id', 'book_id']]
    # renaming the column
    student.rename(columns = {'ID':'id'}, inplace = True)
    # student.replace('', np.nan, inplace=True)

    # generating school and books column
    school = df[['school_id','school']]
    book = df[['book_id','books']]

    # remove duplicate and null rows
    school = school.drop_duplicates(subset='school', keep="first") 
    # school['school'].replace('', np.nan, inplace=True)
    school.dropna(inplace=True)

    book = book.drop_duplicates(subset='books', keep="first")
    # book['books'].replace('', np.nan, inplace=True)
    book.dropna(inplace=True)

    # assigning unique id to school_id column
    # school = school.reset_index()
    # school.drop(columns='school_id', inplace=True)
    # school.rename(columns={"index":"school_id"}, inplace=True)

    # assigning unique id to book_id column
    # book = book.reset_index()
    # book.drop(columns='book_id', inplace=True)
    # book.rename(columns={"index":"book_id"}, inplace=True)

    # renaming the column
    school.rename(columns = {'school':'school_name'}, inplace = True)
    book.rename(columns = {'books':'book_name'}, inplace = True)

    return student, school, book


def insert_to_db(table_data):

    engine = create_engine(r'postgresql://testuser:testpassword@localhost/testdb', echo=False)

    c = engine.connect()
    conn = c.connection

    for table_name, table_values in table_data.items():
        # df = psql.read_sql("SELECT * FROM tabletest", con=conn)  
        table_values.to_sql("library_"+table_name, con=engine, schema=None, index=False, if_exists='append', method="multi")
        # print(df)  
        # df.to_sql(book_data, engine,schema=None)

    conn.close()

    return True


if __name__=='__main__':
    file_name = 'Data.xls'
    student, school, book = eda(file_name)

    print(student)

    insert_to_db({"school": school, "book": book, "student": student})
    # insert_to_db({"student": student})


