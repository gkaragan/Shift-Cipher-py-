# Shift Cipher Encryption/Decryption
This project allows for the encryption and decryption of messages that can be sent between users.
In practice, two individuals say Alice and Bob, would like to communicate with each other over long distances (say via email). However, another individual, Eve, is a spy: she can see every message that is sent between Alice and Bob. In order to keep the content of the messages hidden, or private, Alice and Bob will need to encrypt their messages. Lets start with Alice: she has a message and is ready to send it to Bob; so, she encrypts her message, and sends it over. Alice must also give Bob some additional information that can be used to decrypt the message (this is called a private key). This private key should be kept a secret between Alice and Bob, since if Eve has it, then she can decrypt the message and find its contents. Once Bob receives the message from Alice, he can use this secret private key to decrypt the message and see its original contents. Mathematically, Encryption and Decryption are inverse processes (i.e., if E(m) = e then D(e) = m).
## Description
The project automates the "shift cipher" (Caesar cipher) encryption technique, a well-known encyption method in the field of cryptography.

<img src="https://www.dcode.fr/tools/disk-cipher/images/caesar-disk.png" width=25% height=25%>

Consider the "shift wheel" above. The outer alphabet on the wheel is used to build the original message. Then to encrypt the message, we apply a transformation to the outer alphabet; this is a shift, or turning of the wheel, represented by the inner alphabet. As can be seen from the above picture, if this encryption is applied to the message, A is mapped to Y, B to Z, C to A and so on. This corresponds to a shift of 2 in the clockwise direction.
Of course, to decrypt the message, we shift the inner wheel to its original position, 2 units back in the counterclockwise direction. As one can see, knowing the shift value (private key) makes decrypting the message much easier.
### Functions
This program utilizes two key functions: encrypt and decrypt.

- ```encrypt(message: str)```
  
    The encrypt function handles the automatic encryption of messages. The string module is used to store the characters that will be used for the message and the choice function from the random module randomizes the shift value (private key) upon each message encryption. Note that the shift in the function is applied in the counterclokwise direction, hence, decryption will be in the clockwise direction. A translation table is used instead of looping to improve efficiency, allowing for the transformation to be applied over one pass of the message i.e., 'abc...ABC...012' -> 'bcd...BCD...123' in the case where the shift values are both 1.
    Returns a tuple of the form ('abc', 13, 5), where 'abc' is the encrypted message, 13 is the shift applied to the letters, and 5 is the shift appled to the digits.
  
- ``` decrypt(message: str, letter_shift: int, digit_shift: int)```

    The decrypt function inverts the encryption function, taking the encrypted message as a parameter, along with both of the shift values. The function maps each shifted character back to its original position in the chars string.
Both encrypt and decrypt are called within the main function, depending on whether the user enters '-e' or '-d' in positon 1 of the command line.
When looking to encrypt a message, simply run the program with '-e' entered in the command line and then enter the message when prompted. After the encrypted message is copied and sent, it can be decrypted as follows: run the script with '-d' entered in the terminal and when prompted, enter a tuple of the form ('m', 12, 1), where m is the encrypted message, 12 is the letter shift key, and 1 is the digit shift key. Note that the quotation marks around the message are necessary.
### Aditional Comments
The encryption function randomizes the private keys upon each call, hence, this the keys will need to be provided to the one decrypting the message upon each decryption. In order to choose the keys manually, alter the code by adding two additional parameters to encrypt: "letter_shift", and "digit_shift" and remove the random assignments. This allows the user to pick the shift values and use the same keys for decryption as long as is needed.
