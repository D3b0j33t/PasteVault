# PasteVault CLI

PasteVault is a user-friendly CLI tool for managing Pastebin pastes, with features like paste creation, encryption, and secure configuration.

## Features
- Create, encrypt, and upload pastes to Pastebin.
- Manage privacy settings and expiration dates.
- Store credentials securely in .env

## Installation
1. Clone the repository.

2. Install dependencies:

`pip install -r requirements.txt`

3. Add your credentials to .env.

## Usage
- *Create a paste*:

`python main.py create --name "MyPaste" --content "Hello, world!" --private 1`

- *Create an encrypted paste*:

`python main.py encrypt --name "SecretPaste" --content "Sensitive data"`

- *Delete a paste*:

`python main.py delete --id "12345"`

## License
MIT


How to Run the Project

1. Clone the repository:

`git clone https://github.com/yourusername/PasteVault.git`

`cd PasteVault`

2. Install dependencies:

`pip install -r requirements.txt`

3. Add your credentials to .env.

4. Run the CLI tool:

`python PasteVault/main.py --help`


Now you have a complete and organized PasteVault CLI project!