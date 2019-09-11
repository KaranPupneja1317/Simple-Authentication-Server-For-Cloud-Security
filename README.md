# Simple Cloud Auth Server

## Technologies used
- Flask Framework
- Pip
- Python 3.7
- JavaScript
- HTML, CSS
- Bootstrap

## Pre-requisites for project
- Install Python
- Install Pip
- Install VirtualEnv
- Install VirtualEnvWrapper-win
- Install Flask


## Steps to run Flask
- First install flask using pip,
    `pip install Flask`
    `set FLASK_APP=app.py`
    `flask run`
- Server runs on http://127.0.0.1:5000/ by default


## Structure of project
- **static/** directory contains minified bootstrap css file
- **templates/** directory contains all templates of webpages in html format
- **app.py** file contains core algorithm and route handling
- **file1.txt** file contains userId and username for each account holder
- **file2.txt** file contains userId and password's hash in hex digest format


## How project works
- goto route **/newUser**
- enter username, password, confirm password
- click **Add** button to add a new user

- goto route **/login**
- enter username and password
- click **Login** to login user

- goto route **/updatePassword**
- enter username and old password, new password
- click **Update** to update password


## Error handling
- **front-end validation** submit button remains disabled until all fields are filled properly
- features implemented are:
    - fields should not be empty
    - password should have minimum 8 characters
    - **password** and **confirm password** should match while creating a new user account
    - **old password** and **new password** should not be same while updating password

- **back-end error handling** validations after form submission
- features implemented are:
    - when creating a new user, username should be unique for each account
    - while logging in, if username is not present, **username not found** is displayed
    - and if password is incorrect, **invalid password** is displayed
    - while updating password, error message is displayed for invalid username and password

## MD5 vs SHA1 vs SHA256

+ MD5 

- The MD5 (Message Digest) algorithm is a widely used cryptographic hash function producing a 128-bit (16-byte) hash value, typically expressed in    text format as a 32 digit hexadecimal number. 
- MD5 has been utilized in a wide variety of cryptographic applications, and is also commonly used to verify data integrity.
- MD5 is not collision resistant and several flaws were found in the design of MD5.
- MD5 is considered cryptographically broken and is unsuitable for further use. 

+ SHA1 

- SHA1 (Secure Hash Algorithm) is a cryptographic hash function designed by the National Security Agency (NSA). 
- SHA1 produces a 160-bit (20-byte) hash value, typically rendered as a hexadecimal number, 40 digits long. 
- SHA1 is the most widely used of the existing SHA hash functions, and is employed in several widely used applications and protocols. 
- The SHA1 algorithm might not be secure enough for ongoing use. It is recommended not to use SHA1. 

+ SHA256 

- SHA256 (Secure Hash Algorithm) is a cryptographic hash function designed by the National Security Agency (NSA). 
- SHA256 produces a 256-bit (32-byte) hash value, typically rendered as a hexadecimal number, 64 digits long. 

