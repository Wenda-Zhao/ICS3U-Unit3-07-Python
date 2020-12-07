#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program uses a compound booleam statement


def main():
    # this function uses a compound booleam statement

    # input
    age = int(input("Enter your age: "))
    print("")

    # process & output
    if age > 25 and age < 40:
        print(" Congratulations, you got a date!")
    else:
        print("Sorry, to get a date, you must be over 25 and under 40.")


if __name__ == "__main__":
    main()
