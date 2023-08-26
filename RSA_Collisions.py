from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

def count_unconcealed_messages(p, q, e):
    n = p * q
    unconcealed_count = 0
    for m in range(n):
        encrypted = pow(m, e, n)
        if encrypted == m:
            unconcealed_count += 1
    return unconcealed_count

p = 19
q = 37

unconcealed_counts = []

phi_n = (p - 1) * (q - 1)  # Euler's totient function

for e in range(2, phi_n + 1):
    unconcealed = count_unconcealed_messages(p, q, e)
    unconcealed_counts.append((e, unconcealed))

best_case = max(unconcealed_counts, key=lambda x: x[1])

print("Best case for e:", best_case[0])
print("Number of unconcealed messages:", best_case[1])
