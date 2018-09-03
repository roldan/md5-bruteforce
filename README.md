# md5-bruteforce

Usage

1) Generate wordlist
Edit "tokens" variable of generate_wordlist.py and execute it:

python generate_wordlist.py > wordlist

2) Try to crack password

python md5brute.py HASH wordlist
