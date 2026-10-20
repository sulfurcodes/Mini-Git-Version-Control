import argparse
import sys
from repository import Repository


def main():
    repo = Repository()
    parser = argparse.ArgumentParser(description="Mini Git - By Sulfurcodes")
    subparser = parser.add_subparsers(dest="command", help="Available commands")
    init_parser = subparser.add_parser("init", help="Initialize a new repository")
    add_parser = subparser.add_parser(
        "add", help="Add files and directories to the staging area"
    )
    add_parser.add_argument("paths", nargs="+")
    args = parser.parse_args()

    try:
        if args.command == "init":
            if not repo.init():
                print("Repository already exists")
                return
        elif args.command == "add":
            if not repo.git_dir.exists():
                print("Not a git repository")
                return
            for path in args.paths:
                repo.add_path(path)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    if not args.command:
        parser.print_help()
        return


main()

# testing stuff here
# python src/main.py init
# python src/main.py add src/main.py
