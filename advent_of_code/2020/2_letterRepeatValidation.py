
"""
For example, suppose you have the following list:
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

How many passwords are valid according to their policies?

Input: https://adventofcode.com/2020/day/2/input
"""

from collections import defaultdict, Counter


# READ INPUT:
with open("inputs/2_letterRepeatValidation", "r") as inp:
    rawdata = inp.read().split("\n")[:-1]


def parse(input_list):
    """
    Convert '1-6 m: wermmty' to [m, 1, 6, wermmty]
    Return a list of all such lists
    """
    policy_password_list = []
    for s in input_list:
        key, pswd = s.split(": ")
        limitstr, letter = key.split(" ")
        lo, hi = limitstr.split("-")
        policy_password_list.append([letter, lo, hi, pswd])

    return policy_password_list


def check_validity_old(policy_password_list):
    """
    Input: [ [m, 1, 6, wermmty], [], .. ]
    Returns a list that contains valid passwords
    'wermmty' above is valid because m appears 2 times which is between 1 to 6
    """
    valid_passwords = []
    for pp in policy_password_list:
        letter_counts = Counter(pp[3])
        count = letter_counts.get( pp[0] )

        if not count:
            continue

        if ( count >= int(pp[1]) ) and ( count <= int(pp[2]) ):
            valid_passwords.append( pp[3] )

    return valid_passwords


def check_validity_new(policy_password_list):
    """
    Input: [ [m, 1, 5, wermmty], [], .. ]
    Returns a list that contains valid passwords
    'wermmty' above is valid because m should be present EITHER as 1st letter or 5th (NOT BOTH)
    and 'm; here is present ONLY as 5th letter
    """
    valid_passwords = []
    for pp in policy_password_list:
        letter = pp[0]
        pos1 = int(pp[1]) - 1
        pos2 = int(pp[2]) - 1
        password = pp[3]

        pos1_true = password[pos1] == letter
        pos2_true = password[pos2] == letter

        if (pos1_true + pos2_true) == 1:
            valid_passwords.append( password )

    return valid_passwords



policy_password_list = parse(rawdata)
valid_passwords_old = check_validity_old(policy_password_list)
print("Valid Passwords according to old policy: ", len(valid_passwords_old))
valid_passwords_new = check_validity_new(policy_password_list)
print("Valid Passwords according to new policy: ", len(valid_passwords_new))


