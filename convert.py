# -*- coding: utf-8 -*-
import bit
import time
import hashlib
from bitcoinlib.encoding import addr_bech32_to_pubkeyhash, change_base

input_filename = 'list.txt'
output_filename = 'btcaddress.hex'

def HASH160(pubk_bytes):
    return hashlib.new('ripemd160', hashlib.sha256(pubk_bytes).digest() ).digest()

def save_h160_file(h160_list):
    with open(output_filename, 'a') as f:
        for line in h160_list:
            f.write(line + '\n')

def read_address():
    with open(input_filename) as f:
            coin_list = f.read().rstrip('\n').split('\n')
    print(' Loaded ' + str(len(coin_list)) +' address from file')
    legacy_btc_list = [x for x in coin_list if x[0] == '1']  
    segwit_btc_list = [x for x in coin_list if x[0] == '3']  
    bech32_btc_list = [x for x in coin_list if x[0] == 'b' and len(x) < 45]      
    
    h160_list = [bit.base58.b58decode_check(address)[1:].hex() for address in legacy_btc_list]
    h160_list.extend([bit.base58.b58decode_check(address)[1:].hex() for address in segwit_btc_list])
    save_h160_file(h160_list)
    return h160_list
print(' Will convert Bitcoin address file into hash160.')
h160_list = read_address()
h160_list = set(h160_list)

