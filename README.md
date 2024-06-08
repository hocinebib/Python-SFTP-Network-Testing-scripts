# test

this is a test

gpg --gen-key
subl test_encrypt.txt
gpg --encrypt test_encrypt.txt
subl test_encrypt.txt.gpg
gpg --decrypt test_encrypt.txt.gpg > decrypted
