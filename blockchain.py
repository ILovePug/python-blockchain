genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transaction = []
owner = 'Qian'


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_last_blockchain_value():
    # -1 will give us the last item of the array
    """ returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value 

    Arguments:
        :sender: sender of the coin
        :recipient: the recipient
        :amount: the amount
    """
    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    open_transaction.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(hashed_block)

    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transaction
    }
    blockchain.append(block)


def get_transaction_value():
    tx_recipient = input('Please enter the recipient of the transaction: ')
    tx_amount = float(input('your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('outputting block')
        print(block)


def verify_chain():
    print('im verifying')
    # enumerate will give us a tuple containing index and the value
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False

    return True


waiting_for_input = True

while waiting_for_input:
    print('Please choose: ')
    print('1. Add a newtransaction value')
    print('2. Mine a new block')
    print('3. Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transaction)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == 'h':
        blockchain[0] = {
            'previous_hash': '',
            'index': 0,
            'transactions': [{'sender': 'Chris', 'recipient': 'someone', 'amount': 100}]
        }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a vlaue from the list')
    if not verify_chain():
        print('Invaid blockchain')
        break
else:
    print('user left')
print('Done!')
