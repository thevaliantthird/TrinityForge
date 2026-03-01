from cryptography.fernet import Fernet
import base64
import numpy as np
import pandas as pd



def make_float(results):
    for k, v in results.items():
        for k1, v1 in v.items():
            v1 = v1.astype(np.float64)
            results[k][k1] = v1.sort_index()
    return results

password = ""
key = base64.urlsafe_b64encode(password.encode().ljust(32)[:32])  # very naive but works
f = Fernet(key)

# Encrypt
with open("together_clean.pickle", "rb") as f_in, open("together_clean.pickle.enc", "wb") as f_out:
    f_out.write(f.encrypt(f_in.read()))

# Decrypt
# with open("together_clean.pickle.enc", "rb") as f_in, open("restored.bin", "wb") as f_out:
#     f_out.write(f.decrypt(f_in.read()))