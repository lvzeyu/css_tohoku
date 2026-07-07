#!/usr/bin/env python3
import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Person age calculator example"
    )
    parser.add_argument(
        "--name",
        type=str,
        default="Sato",
        help="Person name"
    )
    parser.add_argument(
        "--birth",
        type=int,
        required=True,
        help="Birth year (e.g. 2000)"
    )
    parser.add_argument(
        "--current-year",
        type=int,
        default=2026,
        help="Current year"
    )
    return parser.parse_args()


def validate_birth_year(birth: int, current_year: int) -> None:
    if birth > current_year:
        raise ValueError("birth year cannot be greater than current year")


def calculate_age(birth: int, current_year: int) -> int:
    return current_year - birth


def build_message(name: str, age: int) -> str:
    return f"Hello, {name}. You are {age} years old."


def main() -> None:
    args = parse_args()
    validate_birth_year(args.birth, args.current_year)
    age = calculate_age(args.birth, args.current_year)
    print(build_message(args.name, age))


if __name__ == "__main__":
    main()

# Run examples:
# python example_argparse.py --birth 2000
# python example_argparse.py --name Marx --birth 1995 --current-year 2026
