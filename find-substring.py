import argparse
import re
import sys
import boto3
from s3 import list_s3_objects, filter_text_objects


def find_substring(substring, bucket_name, text_objects, case_match, exact_match):
    """
    Perform a case sensitive/insensitive, partial/complete substring search depending on the user input within the files of an Amazon s3 bucket. Print the line number for all matches.

    Args:
        substring (str): The substring to find.
        bucket_name (str): The Amazon s3 bucket name.
        text_objects (list[str]): List of s3 text objects.
        case_match (str): Perform case sensitive match.
        exact_match (str): Perform exact match.

    Returns:
        str: A message indicating line numbers for partial and complete matches, or no match is found.
    """
    s3 = boto3.client("s3")
    result = ""

    for object in text_objects:
        response = s3.get_object(Bucket=bucket_name, Key=object)
        # Read the file content line by line
        lines = response["Body"].read().decode("utf-8").split("\n")

        # condition for case sensitive/insensitive match based on user-input
        if case_match == "true":
            pattern_partial = re.compile(re.escape(substring))
            pattern_complete = re.compile(rf"\b{re.escape(substring)}\b")
        else:
            pattern_partial = re.compile(re.escape(substring), re.IGNORECASE)
            pattern_complete = re.compile(rf"\b{re.escape(substring)}\b", re.IGNORECASE)

        # search for partial/exact matches
        partial_matches = []
        complete_matches = []

        for i, line in enumerate(lines, start=1):
            match_partial = pattern_partial.search(line)
            match_complete = pattern_complete.search(line)

            if match_complete:
                complete_matches.append(f"   Exact match at line: {i}")
                continue
            if match_partial:
                partial_matches.append(f"   Partial match at line:  {i}")

        if complete_matches:
            result += f"{object}\n" + "\n".join(complete_matches) + "\n\n"

        # remove partial matches from result based on user-input
        if exact_match == "false":
            if partial_matches:
                result += f"{object}\n" + "\n".join(partial_matches) + "\n\n"

    return result.strip() if result else "No match is found."


def main():
    description = f"""
    Find a substring in s3 objects.\n
    Configure the AWS Credentials: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html"""

    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description=description)

    # Add arguments for bucket, substring, case sensitivity, and exact match
    parser.add_argument(
        "-b", "--bucket", type=str, required=True, help="Amazon s3 bucket name"
    )
    parser.add_argument(
        "-s", "--substring", type=str, required=True, help="search string"
    )
    parser.add_argument(
        "-i",
        "--case",
        choices=["true", "false"],
        default="false",
        type=str,
        required=False,
        help="case-sensitive match",
    )
    parser.add_argument(
        "-e",
        "--exact",
        choices=["true", "false"],
        default="false",
        help="exact word match",
    )

    # Parse the command line arguments
    args = parser.parse_args()

    # check empty search string
    if not args.substring.strip():
        sys.exit(f"Please entry non empty search string")
    if len(args.substring.strip()) >= 100:
        sys.exit(f"Please entry search string < 100 chars")

    s3_objects = list_s3_objects(args.bucket)
    # check if there are objects in s3 bucket
    if s3_objects:
        print("\nGet the list of s3 objects...")
        [print(f"   {obj}") for obj in s3_objects]

        text_objects = filter_text_objects(args.bucket, s3_objects)

        # check if there are text objects in s3 bucket
        if text_objects:
            print("\nFiltered out text objects...")
            [print(f"   {obj}") for obj in text_objects]

            # search for the substring
            print(f"\n---------Search Result For: {args.substring}  ---------")
            result = find_substring(
                args.substring, args.bucket, text_objects, args.case, args.exact
            )
            print(f"\n{result}")
        else:
            print(f"\nError: No Text files found in the s3 bucket: {args.bucket}")
    else:
        print(f"\nError: No files found in the s3 bucket: {args.bucket}")


if __name__ == "__main__":
    main()
