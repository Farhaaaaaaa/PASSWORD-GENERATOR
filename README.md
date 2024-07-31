# PASSWORD-GENERATOR

This is a simple password generator script written in Python. It generates a random password based on a specified length.

## Requirements

- Python 3.x

## Usage

1. **Download the Script**

   Save the script to a file named `password_generator.py`.

2. **Run the Script**

   Open a terminal and navigate to the directory where `password_generator.py` is saved. Then run the script using the following command:

   ```sh
   python password_generator.py
3. **Enter the Desired Password Length**

The script will prompt you to enter the desired length of the password. Type the length and press Enter.

4. **Get Your Password**

The script will generate and print a random password of the specified length




## Explanation

- The script imports the `random` module to enable the selection of random characters.
- `chars` is a string containing all possible characters for the password.
- The user is prompted to enter the desired password length.
- A `for` loop runs for the specified length, selecting a random character from `chars` and appending it to the `password` string.
- Finally, the generated password is printed to the screen.
