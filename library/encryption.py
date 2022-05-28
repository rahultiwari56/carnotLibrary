import os
import json
import random
import base64
import binascii
from django.shortcuts import render

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Library for hashing
from hashlib import sha256

class Encryption():
    """
        class to encrypt and decrypt the data
    """

    def __init__(self):
        self.encryption_key = 'carnot'
        self.key = pad(bytes(self.encryption_key, 'utf-8'),16)


    def genrate_otp(self):
        """
        returns random number of length 5 between 0-9 
        """

        otp=""
        for _ in range (5):
            num=random.randint(0,9)
            otp+= str(num)
        
        return otp


    def CBC_generate_keys(self):
        """
            function to generate random salt and iv

            return (json) : salt and iv values
        """

        salt  = binascii.hexlify(os.urandom(16))
        iv = binascii.hexlify(os.urandom(8))

        key_dict = { 'salt' : salt.decode() , 'iv' : iv.decode()}
        
        return key_dict


    def CBC_decrypt(self , encrypted_data , keys):
        """
        function to decrypt the encrypted data in the CBC mode

            Parameters :
                encrypted_data : encrypted data that you want to decrypt

                return (dic): orginal data

        """
        salt = keys['salt'].encode('utf-8')
        iv = keys['iv'].encode('utf-8')

        data = base64.b64decode(encrypted_data)
        cipher = AES.new(salt, AES.MODE_CBC, iv)
        orginal_data = unpad(cipher.decrypt(data) , 16)
        orginal_data = json.loads(orginal_data.decode('utf-8'))
        return orginal_data


    def ECB_encrypt(self , message , format_type = 'str'):
        """
        function to encrypt the data in the ECB mode

            Parameters:
                message (str / dic) : message to be encrtpted
                format_type : type of encrypted data, by default = 'str'.(Format_type - str or others)
                               other includes - int, tuple , list , dic

            return (json) : encoded admin name and admin password
        """
        if format_type == 'str':
            message = bytes(message, 'utf-8')
            raw_message = pad(message,16)
            cipher = AES.new(self.key , AES.MODE_ECB)
            encoded_message = cipher.encrypt(raw_message)
            return base64.b64encode(encoded_message).decode('utf-8')
            

        elif format_type == 'others':
            json_to_string = json.dumps(message)
            message = bytes(json_to_string, 'utf-8')
            raw_message = pad(message,16)
            cipher = AES.new(self.key , AES.MODE_ECB)
            encoded_message = cipher.encrypt(raw_message)
            return base64.b64encode(encoded_message).decode('utf-8')
        
        else:
            print('data can only be in str or json format')


        
    def ECB_decrypt(self , encrypted_data , format_type = 'str'):
        """
        function to decrypt the encrypted data in the ECB mode

            Parameters :
                encrypted_data : encrypted data that you want to decrypt
                format_type : type of encrypted data, by default = 'str'.(Format_type - str or other)
                              other includes - int, tuple , list , dic

                return : original data

        """
        if format_type == 'str':
            ecrypted_message = base64.b64decode(encrypted_data)
            decryption = AES.new(self.key , AES.MODE_ECB)
            orginal_message = decryption.decrypt(ecrypted_message)
            return unpad(orginal_message , 16).decode('utf-8')

        elif format_type == 'others':
            ecrypted_message = base64.b64decode(encrypted_data)
            decryption = AES.new(self.key , AES.MODE_ECB)
            orginal_message = decryption.decrypt(ecrypted_message)
            return json.loads(unpad(orginal_message , 16).decode('utf-8'))
        
        else:
            print('data can only be in str or json format')


    def hash_encoding(self, data_to_hash):
        """
            I/P: String
            O/P: Returns hashed value(string) of the input
        """
        
        hash_sha256 = sha256()
        hash_sha256.update(bytes(data_to_hash, 'utf-8'))
        hashed_data = hash_sha256.hexdigest()

        return hashed_data


if __name__ == "__main__":
    
    Encryption = Encryption()
    encrypted_data=Encryption.ECB_encrypt(123 , format_type='others')
    print(encrypted_data)
    original_message = Encryption.ECB_decrypt ( encrypted_data , format_type= 'others')
    print(original_message)
    print(type(original_message))

    