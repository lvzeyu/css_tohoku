#!/usr/bin/env python3
import argparse


class Person:
    def __init__(self, name: str, birth: int, current_year: int) -> None:
        self.name = name
        self.birth = birth
        self.current_year = current_year

    def age(self) -> int:
        return self.current_year - self.birth

    def intro_message(self) -> str:
        return f"Hello, my name is {self.name}. I am {self.age()} years old."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Class + argparse example (Person)"
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


def main() -> None:
    args = parse_args()
    validate_birth_year(args.birth, args.current_year)

    person = Person(
        name=args.name,
        birth=args.birth,
        current_year=args.current_year,
    )
    print(person.intro_message())


if __name__ == "__main__":
    main()

# Run examples:
# python example_class_argparse.py --birth 2000
# python example_class_argparse.py --name Marx --birth 1995 --current-year 2026
