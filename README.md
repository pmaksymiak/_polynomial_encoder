
Polynomial Encoder - creates polynomial function that goes through all the specified points (defined int the form of string in python script).

I thought I can use it to pack information, and then later pass  polynomial formula with co-efficients into the decoder, to recreate original message, unfortunetely during decoding due to the polynomial interpolation being not accurate enough - decoding does not work as intended. 

Something like this can be used in Shamir's Secret Sharing scheme.

Shamir's Secret Sharing scheme is a cryptographic method used to divide a secret into multiple parts, called shares. It was introduced by Adi Shamir in 1979. The scheme allows a secret to be distributed among a group of participants, such that only a specified number of them are needed to collaborate to reconstruct the secret. This threshold-based approach provides a way to securely store or transmit sensitive information without relying on a single point of failure.

The main idea behind Shamir's Secret Sharing scheme is polynomial interpolation. The process involves the following steps:

Choose a threshold value (t): This is the minimum number of participants needed to reconstruct the secret. For example, if t=3, then at least three participants must collaborate to recover the secret.

Encode the secret: The secret (S) is encoded as the constant term in a polynomial of degree (t-1). The other coefficients are randomly chosen. For example, if t=3, a quadratic polynomial is used: P(x) = a0 + a1x + a2x^2, where a0 is the secret (S), and a1 and a2 are random coefficients.

Generate shares: Compute the value of the polynomial P(x) at different points (x ≠ 0). Each point (x, P(x)) is a share of the secret. Distribute these shares among the participants.

Reconstruct the secret: To reconstruct the secret, at least t participants must pool their shares. Using their shares as data points, they can apply polynomial interpolation techniques, such as Lagrange interpolation, to reconstruct the original polynomial and thus obtain the secret (S) as the constant term a0.

Shamir's Secret Sharing scheme has several desirable properties:

Security: No group of fewer than t participants can gain any information about the secret.
Flexibility: The threshold value t can be chosen to accommodate different security requirements.
Scalability: The scheme can handle any number of participants, with each participant receiving one share.
This method is used in various applications, such as secure key management, backup systems, distributed signature schemes, and secure multi-party computation.


![ Polynomial Encoder ](_poly_encoder.JPG)
