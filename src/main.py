from uuid import uuid4

from flask import Flask, request, jsonify

from utils.validate import Validate
from utils.hash import Hash

from model.blockchain import Blockchain
from model.block import Block

from utils.proof_of_work import ProofOfWork
from constants.constants import Constants

app = Flask(__name__)
blockchain = Blockchain()

node_identifier = str(uuid4())

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    value = request.get_json()

    if not Validate.is_valid_request(value):
        return 'Missing parameters', 400

    block = Block(value['sender'], value['recipient'], value['amount'])
    index = blockchain.create_transaction(block)

    response = {
        'message': 'New transaction added to block ' + str(index)
    }

    return jsonify(response), 201


@app.route('/mining', methods=['GET'])
def mining():
    last_chain_block = blockchain.get_last_block
    last_proof = last_chain_block['proof']

    proof = ProofOfWork.proof_of_work(last_proof)

    # Rewarding the miner
    blockchain.create_transaction(
        sender=Constants.REWARDED_MINER,
        recipient=node_identifier,
        amount=Constants.REWARD_VALUE
    )

    # Add mined block to the chain
    previous_block_hash = Hash.hash_block(last_chain_block)
    block = blockchain.create_block(proof, previous_block_hash)

    response = {
        'message': 'New block forged to the chain',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_block_hash': block['previous_block_hash']
    }

    return jsonify(response), 200


@app.route('/chain', methods=['GET'])
def see_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }

    return jsonify(response), 200


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=1337)