import requests
from urllib import response

def get_student_data(endpoint):
    '''
        This function is just used for testing purpose for api call 
    '''
    # get_response = requests.get(endpoint, params={"abc": 123}, json={"query":
    # "Hello peeps!!"})
    get_response = requests.get(endpoint)
    print(response, end='\n\n')

    print(get_response.headers, end='\n\n')
    # print(get_response.text) # return the text response
    print(get_response.json())
    print(get_response.status_code)
    

if __name__=='__main__':
    endpoint = "http://127.0.0.1:8000/get-student/2"
    get_student_data(endpoint)
