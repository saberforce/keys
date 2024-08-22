import rsa
import hashlib
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)
@app.route("/")

def generateKeys():

    public_key, private_key = rsa.newkeys(2048)
    # with open("public.pem", "wb") as f:
    #     f.write(public_key.save_pkcs1("PEM"))

    # with open("private.pem","wb") as f:
    #     f.write(private_key.save_pkcs1("PEM"))
    # #
    # with open("private.pem", "rb") as f:
    #     private_key=(rsa.PrivateKey.load_pkcs1(f.read()))
    # with open("public.pem", "rb") as f:
    #     public_key=(rsa.PublicKey.load_pkcs1(f.read()))

    # with open("private.pem", "rb") as f:
    #     private_key=f.read()
    # with open("public.pem", "rb") as f:
    #     public_key=f.read()


    # print(public_key)
    # print(private_key)

    return {"public_key": str(public_key), "private_key": str(private_key)}




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
