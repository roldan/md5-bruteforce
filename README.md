# md5-bruteforce

## Usage

1. Edit "tokens" variable of generate_wordlist.py and execute to generate a wordlist:

`python generate_wordlist.py > wordlist`

2. Try to crack password comparing MD5 hash of each item in WORDLIST against HASH

`python md5brute.py HASH wordlist`
