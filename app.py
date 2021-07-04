# app.py

import os
import json
import boto3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

from flask import Flask, jsonify, request
app = Flask(__name__)

CLIENT_KEYS_TABLE = os.environ['CLIENT_KEYS_TABLE']
client = boto3.client('dynamodb')


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/client_keys/<string:client_id>")
def get_user(client_id):
    resp = client.get_item(
        TableName=CLIENT_KEYS_TABLE,
        Key={
            'client_id': { 'S': client_id }
        }
    )
    item = resp.get('Item')
    if not item:
        return jsonify({'error': 'User does not exist'}), 404

    priv_key = item.get('client_priv_key').get('B')
    return_priv_key = priv_key.decode('utf-8')

    return jsonify({
        'client_id': item.get('client_id').get('S'),
        'client_priv_key': return_priv_key
    })


@app.route("/client_keys", methods=["POST"])
def create_client_keys():
    client_id = request.json.get('client_id')
    #name = request.json.get('name')
    if not client_id:
        return jsonify({'error': 'Please provide client_id'}), 400

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
        )
        
    public_key = private_key.public_key()

    priv_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
        )
    
    pub_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    resp = client.put_item(
        TableName=CLIENT_KEYS_TABLE,
        Item={
            'client_id': {'S': client_id },
            'client_priv_key': {'B': priv_pem }
        }
    )

    return jsonify({
        'client_id': client_id,
        'client_pub_key': pub_pem.decode('utf-8')
    })
