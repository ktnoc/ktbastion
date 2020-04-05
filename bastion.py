from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Protocol.KDF import scrypt

from datetime import datetime
import sys, getopt, json, os, base58

def decode(filename,password,subaction,subparam,opts):
    if password is None:
        password = input("Enter password :\n")

    f = open(filename,"r")
    data = f.read()

    decoded = base58.b58decode(data)

    iv = decoded[:16]
    ciphered_data = decoded[16:-32]
    salt = decoded[-32:]
#    key = PBKDF2(password, salt, dkLen=32)
    key = scrypt(password, salt, 32, N=2**20, r=8, p=1)
    cipher_decrypt = AES.new(key, AES.MODE_CBC,iv=iv)
    original_data = unpad(cipher_decrypt.decrypt(ciphered_data), AES.block_size)

    f.close()
    
    data = json.loads(original_data.decode("utf-8"))
    
    if len(data) == 0 and not subaction == "add":
        print("empty file")
    else:
        print(subaction)
        if subaction == "list": 
            keylist = list(data.keys())
            print("Key list :", keylist)
        if subaction == "view":
            print("Viewing", subparam)
            print(data[subparam]['keys'])
        if subaction == "remove":
            if subparam in data:
                del data[subparam]
                final = bytes(json.dumps(data).encode("utf-8"))
                save(password,filename,final)
        if subaction == "add":
            if not subparam in data:
                print(subparam)
                for opt, arg in opts:
                    if opt in ("-k", "--key"):
                        now = datetime.now()
                        new_dict = {}
                        new_dict[subparam] = {}
                        new_dict[subparam]["keys"] = arg.split(',')
                        new_dict[subparam]["date"] = str(now.day)+'/'+str(now.month)+'/'+str(now.year) 
#                        print(new_dict)
                        data.update(new_dict)
                        final = bytes(json.dumps(data).encode("utf-8"))
                        save(password,filename,final)

def save(password,filename,data=''):
    data = bytes(data)

    salt = get_random_bytes(32)
#    key = PBKDF2(password, salt, dkLen=32)
    key = scrypt(password, salt, 32, N=2**20, r=8, p=1)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    encoded = base58.b58encode(iv+ciphered_data+salt).decode("utf-8")

    f = open(filename,"w+")
    f.write(str(encoded))
    f.close()

def create(filename,password):
    print("create",filename)
    salt = get_random_bytes(32)
    if password is None:
        password = input("Enter password :\n")

    data = b'{}'

#    key = PBKDF2(password, salt, dkLen=32)
    key = scrypt(password, salt, 32, N=2**20, r=8, p=1)
    cipher = AES.new(key, AES.MODE_CBC)
    ciphered_data = cipher.encrypt(pad(data, AES.block_size))
    iv = cipher.iv
    encoded = base58.b58encode(iv+ciphered_data+salt).decode("utf-8")

    f = open(filename,"w+")
    f.write(str(encoded))
    f.close()

def invalid_command(argv):
    print("Invalid command '",*argv,"' type '--help' for a list.")
    sys.exit(2)

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hc:d:p:a:lr:v:k:",["help","create=","decode=","password=","add=","list","remove=","view=","key="])
    except getopt.GetoptError:
        invalid_command(argv)
    filename = action = password = subaction = subparam = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("""
    Command line options:
       -c [--create] <new_bastion_file> : create a new bastion
       -d [--decode] <existing_bastion_file> : use a bastion file
     """)
            sys.exit()
        elif opt in ("-c","--create"):
            action = "create"
            if os.path.exists(arg):
                print(arg,"already exists, exiting")
                sys.exit()
            else:
                filename = arg
        elif opt in ("-d", "--decode"):
            action = "decode"
            if os.path.exists(arg):
                filename = arg
            else:
                sys.exit()
        elif opt in ("-p", "--password"):
            password  = arg
        elif opt in ("-a", "--add"):
            subaction = "add"
            subparam = arg
            #print(opts)
        elif opt in ("-l", "--list"):
            subaction = "list"
        elif opt in ("-r", "--remove"):
            subaction = "remove"
            subparam = arg
        elif opt in ("-v", "--view"):
            subaction = "view"
            subparam = arg

    if action == "create":
        create(filename,password)
    elif action == "decode":
        if not subaction is None:
            decode(filename,password,subaction,subparam,opts) 
if __name__ == "__main__":
   main(sys.argv[1:])

