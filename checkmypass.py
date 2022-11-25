import requests
import sys
import hashlib

def make_request(pass_hash_head, pass_hash_tail):
    url = "https://api.pwnedpasswords.com/range/" + pass_hash_head
    res = requests.get(url)
    all_matches = res.text.splitlines()
    for match in all_matches:
        if(match.split(":")[0] == pass_hash_tail.upper()):
            seen_count = match.split(":")[1]
            return(f"This password has been seen {seen_count} times before! You should change it.")
    return("No match found! You can keep using this.")

def process_pass(password):
    byte_pass = bytes(password, "utf-8")
    hash_pass = hashlib.sha1(byte_pass).hexdigest()
    pass_hash_head = hash_pass[:5]
    pass_hash_tail = hash_pass[5:]
    print(make_request(pass_hash_head, pass_hash_tail))


process_pass(sys.argv[1])