# Overview:
The Python Substring Search Script is a powerful tool designed to effortlessly search through the contents of an Amazon S3 bucket, providing users with a versatile and efficient means of locating specific substrings. This script combines simplicity with advanced search functionalities, allowing for case-insensitive searches, exact word matches, and even the ability to search for entire phrases within the stored data.

<h3>Key Features:</h3>

<h4>Case-Insensitive Search:</h4>
The script enables users to perform case-insensitive searches, ensuring that matches are found regardless of letter casing. This feature enhances the flexibility of the search, accommodating various input formats and preferences.

<h4>Exact Word Search:</h4>
Users can conduct searches for exact word matches, filtering out partial matches and returning only instances where the specified substring appears as a whole word. This ensures precision and accuracy in search results.

<h4>Phrase Search:</h4>
The script supports the search for entire phrases, allowing users to locate specific sequences of words within the S3 bucket contents. This feature is particularly useful for pinpointing contextual information and finding comprehensive data sets.

<h4>Efficient Amazon S3 Integration:</h4>
The script seamlessly interacts with the Amazon S3 API, retrieving data efficiently and minimizing latency. It utilizes the Boto3 library to establish a secure connection to the S3 bucket, ensuring a smooth and reliable search experience.

<h4>User-Friendly Command-Line Interface (CLI):</h4>
The script boasts a user-friendly CLI that facilitates easy input of search parameters. Users can specify the substring, choose the search type (case-insensitive, exact word, or phrase), and provide the S3 bucket details with minimal effort.

<h4>Detailed Search Results:</h4>
Upon completion of the search, the script provides detailed results, including the file paths. This allows users to quickly identify and access the relevant information within the S3 bucket.

<h3>How to Use:</h3>
<h4>Installation:</h4>
Clone the repo and install the required dependencies, including Boto3, using a package manager such as pip.<br>

```
pip3 install -r requirements.txt
```

<h4>AWS Authentication:</h4>
Configure the AWS CLI Credentials or use short lived credentials from AWS SSO <br> 
  - https://docs.aws.amazon.com/cli/latest/userguide/cli-authentication-short-term.html <br>
  - https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html

<h4>Command-Line Interface:</h4>
Use the intuitive CLI to input search parameters, specifying the substring and desired search type.

```
python3 find-substring.py -b <s3-bucket-name> -s <substring>
```

<h4>Review Results:</h4>
The script will display comprehensive results, making it easy for users to navigate and access the identified substrings within the Amazon S3 bucket.

<h4>Conclusion:</h4>
The Python Substring Search Script for Amazon S3 streamlines the process of locating specific substrings within large datasets. With its versatile search capabilities and seamless integration with Amazon S3, this script empowers users to efficiently extract valuable information from their cloud storage, enhancing productivity.
