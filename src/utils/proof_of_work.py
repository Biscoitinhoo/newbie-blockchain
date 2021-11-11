import hashlib

class ProofOfWork():
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof


    @staticmethod
    def valid_proof(last_proof, proof):
        value_to_guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(value_to_guess).hexdigest()

        return guess_hash[:4] == "0000"