import hashlib

class ProofOfWork():

    def validate_transaction(self, last_proof):
        print('Mining started.')

        proof = 0
        while self.__valid_proof(last_proof, proof) is False:
            proof += 1

        print('Mining done with success. Proof: ' + str(proof))
        print('Chain added to the blockchain.')
        
        return proof


    @staticmethod
    def __valid_proof(last_proof, proof):
        value_to_guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(value_to_guess).hexdigest()

        return guess_hash[:4] == "0000"