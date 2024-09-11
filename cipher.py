def c_encrypt(p: str,s:int)->str:
    """Function for caesar cipher encryption and return string value
        
        Formular: 
            cipher_text = (plain_text + shift) mod 26
    
        plain_text(string) : a string of plain text

        shift(int) : number of shift and non-negative 
        
        shifted(int): shifted number 
        
        Returns:
            string of cipher text 

        praise:
            shift must be non negative integer value 

        If statements ensure character is in lower case or upper case
        if shifted is larger than z and Z in ascii character. shifted will substracted -26
    
    
    """
    cipher_text=""
    if shift < 0:
        raise ValueError("Shift value is below zero !!!")
    
    for char in plain_text:
        
        if char.islower():
            shifted = ord(char)+shift  
            if shifted  > ord('z'):  
                shifted =shifted - 26
            cipher_text +=chr(shifted)    
        elif char.isupper(): 
            shifted =ord(char) +shift
            if shifted  > ord('Z'): 
                shifted = shifted - 26
            cipher_text +=chr(shifted)
        else:
            cipher_text +=char
    return cipher_text
  

def c_decrypt(cipher_text:str,shift:int)->str:
    """Function for caesar cipher decryption and return string value

        Formular: 
            decipher_text = (cipher_text - shift) mod 26
            key_index = 
       
       Arguments: 

       cipher_text (string): cipher text from  the c_encrypt 

       shift(int): shift value is non-negative value

       shifted(int): shifted value 

       Return: 
       
           Return strings of decrypted string 

       praise: 
             shift must be non negative integer value
       If statements ensure character is in lower case or upper case
        if shifted is larger than z and Z in ascii character. shifted will substracted -26
       
    """
    
 
    if shift < 0:
        raise ValueError("Shift value is below zero !!!")

    decipher_text= ""
    for char in cipher_text:
        if char.islower(): 
            shifted= ord(char) -shift
            if shifted <ord('a'):
                shifted =shifted +26 
            decipher_text +=chr(shifted)
        elif char.isupper(): 
            shifted = ord(char) -shift
            if shifted <ord('A'):
                shifted = shifted +26
            decipher_text +=chr(shifted)
        else:
            decipher_text +=char
    return decipher_text

def v_encrypt(plain_text:str,key:str)->str: 
   """Function for viegrenere encrypt and return value of string
    Args: 
        plain_text(string) : plain text 
        
        cipher_text: cipher text for encryption
        
        key(string): key 
        
        Key(int ): key index 

        key_len: (int): length of key
    
    Return: 
        return string of viegrenere encryotion

    praise: 
        key value must be alphabet variable 

   
   """
   cipher_text =""
   key_index= 0
   key_len = len(key)
   if not key.isalpha():
       raise ValueError("key is not valid")
   
   
   for char in plain_text:
       if char.islower():
           shift= ord(key[key_index]) - ord('a')
           cipher_text+=c_encrypt(char,shift) 
           key_index = key_index + 1 %key_len
       elif char.isupper():
           shift = ord(key[key_index])- ord('A')
           cipher_text +=c_encrypt(char,shift)
           key_index = key_index +1 %key_len
       else:
           cipher_text +=char
   return cipher_text

def v_decrypt(cipher_text:str,key:int)->str: 
   """Function for viegrenere dencrypt and return string value
    cipher_text: cipher_text from v_encrypt 
    
    decipher_text: decrypt text from cipher text 

    key(string): key 
        
    Key(int ): key index 

    key_len: (int): length of key

     Return: 
        return string of viegrenere encryotion
    
    praise: 
        key value must be alphabet variable 

        cipher_text can be upper or lower
   """
   
   decipher_text=""
   key_index =0 
   key_len = len(key) 

   if not key.isalpha():
       raise ValueError("key is not valid")
 
   for char in cipher_text:
       
       if char.islower(): 
           shift = ord(key[key_index]) - ord('a') 
           decipher_text+=c_decrypt(char,shift)
           key_index =key_index +1 %key_len
       elif char.isupper():
           shift = ord(key[key_index])-ord('A') 
           decipher_text +=c_decrypt(char,shift)
           key_index = key_index + 1 %key_len
       else:
           decipher_text +=char
   return decipher_text

   
print("Caesar cipher")
plain_text ="HELLOWORLD"
shift = 3
cipher= c_encrypt(plain_text,shift)
decipher= c_decrypt(cipher,shift)
print(f"plain text:{plain_text}")
print(f"shifted: {shift}")
print(f"encrypt:{cipher}" )
print(f"decrypt: {decipher}")

print("viegrene Cipher:")
plain_text="he llo"
key = "abcde"
print(f"plain text: {plain_text}")
print(f"key: {key}")
cipher = v_encrypt(plain_text,key)
decipher = v_decrypt(cipher,key)
print(f"viegrene encrypt: {cipher}")
print(f"viegrene decrypt: {decipher}")

