import argparse
from pastebin import PastebinManager
from encryption import encrypt_text
from config_manager import ConfigManager

def main():
    # Parse CLI arguments
    parser = argparse.ArgumentParser(
        description="PasteVault: A secure and user-friendly CLI tool for managing Pastebin pastes."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Sub-command: Create Paste
    create_parser = subparsers.add_parser("create", help="Create a new paste")
    create_parser.add_argument("--name", required=True, help="Name of the paste")
    create_parser.add_argument("--file", help="Path to the file to upload")
    create_parser.add_argument("--content", help="Content to paste (overrides file if provided)")
    create_parser.add_argument("--private", type=int, choices=[0, 1, 2], default=0, help="Paste privacy (0=public, 1=unlisted, 2=private)")
    create_parser.add_argument("--expire", default="N", help="Paste expiration (e.g., 10M, 1D)")

    # Sub-command: Encrypt and Upload
    encrypt_parser = subparsers.add_parser("encrypt", help="Create an encrypted paste")
    encrypt_parser.add_argument("--name", required=True, help="Name of the paste")
    encrypt_parser.add_argument("--content", required=True, help="Content to encrypt and upload")

    # Sub-command: Delete Paste
    delete_parser = subparsers.add_parser("delete", help="Delete an existing paste from Pastebin")
    delete_parser.add_argument("--id", help="The unique ID of the paste to delete")
    delete_parser.add_argument("--name", help="The name of the paste to delete (alternative to ID)")

    # Parse the arguments
    args = parser.parse_args()

    # Load configuration
    config = ConfigManager.load_config()

    # Handle commands
    pastebin = PastebinManager(config["api_dev_key"], config["api_user_name"], config["api_user_password"])
    if args.command == "create":
        content = args.content or open(args.file).read()
        url = pastebin.create_paste(content, args.name, args.private, args.expire)
        print(f"Paste created: {url}")

    elif args.command == "encrypt":
        encrypted_content = encrypt_text(args.content)
        url = pastebin.create_paste(encrypted_content, args.name, private=2)
        print(f"Encrypted paste created: {url}")

    elif args.command == "delete":
        if args.id:
            pastebin.delete_paste(args.id)
            print(f"Paste with ID '{args.id}' deleted successfully!")
        elif args.name:
            paste_id = pastebin.get_paste_id_by_name(args.name)
            if paste_id:
                pastebin.delete_paste(paste_id)
                print(f"Paste with name '{args.name}' (ID: {paste_id}) deleted successfully!")
            else:
                print(f"No paste found with name '{args.name}'")
        else:
            print("Error: You must specify either --id or --name to delete a paste.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
