## Newbie-Blockchain

While explaining how a Blockchain works, I created a simple one to simulate monetary transaction. There's a lot of things to be implemented, but I didn't do it
yet because I didn't need it for the explanation :P.

I was also planning to explain how a Blockchain works on this README, but I would be reinventing the wheel since there's a lot of good content about this on the
internet (like the [Ethereum posts](https://ethereum.org/en/)).

### There are 3 paths:


    To see the entire Blockchain.
    [GET] http://192.168.1.11:1337/
    
    To validate and forge a Block to the chain using POW mechanism.
    [GET] http://192.168.1.11:1337/mine
   
    To create a new transaction to a Block.
    [POST] http://192.168.1.11:1337/transactions/new
    
    
 Create as many transactions as you want and, for validate them, use the ```/mine``` path.
 
 ### Body for transactions:
 
    {
      "sender": "sender-address",
      "recipient": "recipient-address",
      "amount": 3
    }
