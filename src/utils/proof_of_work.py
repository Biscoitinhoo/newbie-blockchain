import hashlib

class ProofOfWork():

    @staticmethod
    def proof_of_work(self, last_proof):
        print('Mining started.')

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        print('Mining done with success. Proof: ' + proof)
        return proof


    @staticmethod
    def valid_proof(last_proof, proof):
        value_to_guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(value_to_guess).hexdigest()

        return guess_hash[:4] == "0000"