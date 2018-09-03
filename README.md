# md5-bruteforce

## Usage

1. Edit "tokens" variable of generate_wordlist.py and execute to generate a wordlist:

`python generate_wordlist.py > wordlist`

2. Try to crack password comparing MD5 hash of each item in WORDLIST against HASH

`python md5brute.py HASH wordlist`


*'md5brute.py' was taken from https://www.phillips321.co.uk/2013/08/31/multi-threading-python-a-quick-example/*
