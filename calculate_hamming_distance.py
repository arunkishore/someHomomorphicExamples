from phe import paillier
import numpy as np

public_key, private_key = paillier.generate_paillier_keypair()

n = 1000
hotencoded_data_1 = [0,0,1,0,1]
hotencoded_data_2 = [0,1,0,0,0]#np.random.randint(2,size=(n,))

def encrypt(public_key,data):
    return [public_key.encrypt(x) for x in data]


encrypted_data_1 = encrypt(public_key,hotencoded_data_1)
encrypted_data_2 = [public_key.encrypt(x) for x in hotencoded_data_2]


def hammingDistanceSuperSimple(str1,str2):
    return np.count_nonzero(np.asarray([private_key.decrypt(x) for x in list(str1 - str2)]))

print(hammingDistanceSuperSimple(np.asarray(encrypted_data_1),np.asarray(encrypted_data_2)))


##### to time the individual functions
#ref: http://pythoncentral.io/time-a-python-function/

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

wrapped = wrapper(encrypt, public_key, hotencoded_data_1)

no_repeats = 1000
print("time to execture the code once",(timeit.timeit(wrapped,number=no_repeats))/no_repeats)

