class Validate():
    @staticmethod
    def is_valid_request(request):
        # Required JSON structure for post a new transaction.
        required_values = ['sender', 'recipient', 'amount']
        
        if not all(x in request for x in required_values):
            return False

        return True