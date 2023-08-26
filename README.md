# RSA Encryption: Unconcealed Messages and Overview

RSA (Rivest–Shamir–Adleman) is a widely used public-key cryptosystem that provides a secure method for data encryption and digital signatures. This README dives into an intriguing facet of RSA known as "unconcealed messages" and offers a comprehensive overview of RSA encryption.

## Table of Contents
- [Introduction to RSA Encryption](#introduction-to-rsa-encryption)
- [Unconcealed Messages in RSA](#unconcealed-messages-in-rsa)
- [How Does RSA Work?](#how-does-rsa-work)
- [Calculating Unconcealed Messages](#calculating-unconcealed-messages)
- [Using the Provided Code](#using-the-provided-code)
- [Contributing](#contributing)
- [Resources](#resources)
- [License](#license)

## Introduction to RSA Encryption

RSA is a fundamental asymmetric encryption algorithm invented by Ron Rivest, Adi Shamir, and Leonard Adleman in 1977. It's based on the mathematical properties of large prime numbers and modular arithmetic. RSA enables secure communication by allowing two parties to exchange data in such a way that even if intercepted, the data remains confidential.

## Unconcealed Messages in RSA

### Exploring the Quirk

While RSA is renowned for its security features, there exists a quirk known as "unconcealed messages." These are messages that remain unchanged after being encrypted using the RSA algorithm. Specifically, for certain values of the public exponent "e," the encryption operation (m^e mod n) doesn't alter the message "m."

### Significance and Implications

The existence of unconcealed messages isn't a security flaw but rather a fascinating mathematical property. It highlights the intricate relationship between the encryption exponent, modulus, and the nature of the message being encrypted. Understanding this phenomenon is crucial for grasping the nuances of RSA and its limitations.

## How Does RSA Work?

RSA encryption involves a pair of keys: a public key and a private key.

### Public Key
The public key comprises two components: the modulus "n" and the encryption exponent "e." The modulus is the product of two large prime numbers, often denoted as "p" and "q." The encryption exponent "e" is chosen to be relatively prime to the totient of "n."

### Private Key
The private key also includes the modulus "n," but it employs a different exponent known as the decryption exponent "d." The relationship between "e" and "d" ensures that decrypting an encrypted message yields the original plaintext.

## Calculating Unconcealed Messages

To identify the best and worst cases for "e" in terms of unconcealed messages, a computational analysis is necessary.

### Code Implementation

The provided Python script (`RSA_Collisions.py`) calculates the number of unconcealed messages for different values of "e" within a specified range. It uses the `cryptography` library to facilitate RSA operations.

### Exploring Different Scenarios

Feel free to modify the script parameters, such as the prime numbers "p" and "q," to observe how unconcealed messages vary with different inputs. This experimentation can deepen your understanding of the RSA algorithm's intricacies.

## Using the Provided Code

1. Install the required library using `pip install cryptography`.

2. Run the Python script `RSA_Collisions.py`.

3. Observe the calculated results to understand the relationship between "e" and unconcealed messages.

## Contributing

Contributions to this repository are welcomed and encouraged. Whether you're correcting typos, improving code efficiency, or adding explanatory content, your contributions help enhance the educational value of this resource.

## Resources

For those seeking a more comprehensive grasp of RSA and cryptography, the following resources are recommended:

- [RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_%28cryptosystem%29) on Wikipedia
- [Cryptography and Network Security: Principles and Practice](https://www.amazon.com/Cryptography-Network-Security-Principles-Practice/dp/0134444280) by William Stallings

## License

This project is licensed under the MIT License. To learn more, refer to the [LICENSE](LICENSE) file.

As you delve into the intricate world of RSA encryption, the phenomenon of unconcealed messages offers a glimpse into the underlying mathematical concepts. This README aims to provide a solid starting point for comprehending RSA, its quirks, and its role in securing digital communication.
