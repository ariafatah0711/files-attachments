from Crypto.Util.number import getPrime, bytes_to_long

p = getPrime(1024)
q = getPrime(1024)
n = p * q
e = 3
m = bytes_to_long(open('flag.txt', 'rb').read())

c = pow(m, e, n)
c_bonus = pow(2*m + 1, e, n)

print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
print(f'BONUS = {c_bonus}')
