from termcolor import colored
import hashlib


def tryopen(path):
    global pass_file
    try:
        pass_file = open(path, 'r')
    except:
        print("could not open the file ")
        quit()


pass_hash = input("Enter MD5 value:")
wordlist = input("Enter Wordlist name:")

# 61243c7b9a4022cb3f8dc3106767ed12
# The short answer is: both exit() and quit() are instances of the same Quitter class, the difference is in naming only, that must be added to increase user-friendliness of the interpreter.
tryopen(wordlist)

for word in pass_file:
    print(colored("[+] trying " + word.strip('\n'), 'red'))
    word_enc = word.encode('utf-8')
    # https://www.programiz.com/python-programming/methods/string/encode
    # should world encrypt to 8 bits before enctryption should encode then md5
    # hashlih.md5 == create a object to make hashing md5 we call hexdigest
    md5digest = hashlib.md5(word_enc.strip()).hexdigest()
    if pass_hash == md5digest:
        print(colored("Found The Passsword :" + word, "green"))
        exit(0)
