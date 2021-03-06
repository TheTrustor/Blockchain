import datetime
import hashlib
import json
from flask import Flask, jsonify


class Blockchain:

    def __init__(self):
        self.chain = []
        self.create_block(proof = 1, previous_hash = '0')

    def create_block(self, proof, previous_hash):
        block = {'index' : len(self.chain)+1,#Length of the chain created in the __init__ function
                'timestamp' : str(datetime.datetime.now()),
                'proof' : proof,
                'previous_hash' : previous_hash}
        self.chain.append(block)
        return block

    def get_latest_block(self): 
        return self.chain[-1] # -1 to return the last block