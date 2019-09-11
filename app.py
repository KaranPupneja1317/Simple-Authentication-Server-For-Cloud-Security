from flask import Flask, render_template, redirect, url_for, request

# create the application object
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('./home.html')


##############################################################################
@app.route('/userLogin')
def userLogin():
    return render_template('./userLogin.html')


@app.route('/userLogin', methods=['POST'])
def userLoginPost():
    username = request.form['username']
    password = request.form['password']
    msg = userLoginDriver(username, password)
    return msg


# main driver function
def userLoginDriver(username, password):
    userId = getUserId(username)
    if not userId:
        return "username not found"
    cipher = str(password) + str(userId)
    import hashlib
    hashedData = hashlib.sha256(cipher.encode())
    if checkPassword(userId, hashedData):
        return "login successful"
    else:
        return "invalid password"
        

# getting userId of username (returns None if not found)
def getUserId(username):
    fp = open("file1.txt", "r")
    dataLine = fp.readline()
    userId = None
    while(dataLine):
        uname = dataLine.split(",")[1]
        uname = uname.replace("\n", "")
        if uname == username:
            userId = dataLine.split(",")[0]
        dataLine = fp.readline()
    fp.close()
    return userId


# checking if password exist for userId
def checkPassword(userId, hashedData):
    fp = open("file2.txt", "r")
    string = str(userId) + "," + str(hashedData.hexdigest())
    dataLine = fp.readline()
    passwordFound = False
    while(dataLine):
        dataLine = dataLine.replace("\n", "")
        if dataLine == string:
            passwordFound = True
        dataLine = fp.readline()
    fp.close()
    return passwordFound


##############################################################################
@app.route('/updatePassword')
def updatePassword():
    return render_template('./updatePassword.html')


@app.route('/updatePassword', methods=['POST'])
def updatePasswordPost():
    username = request.form['username']
    oldPassword = request.form['oldPassword']
    newPassword = request.form['newPassword']
    msg = updatePasswordDriver(username, oldPassword, newPassword)
    return msg


# before ensure user is logged in

# main driver function
def updatePasswordDriver(username, password, newPassword):
    userId = getUserId(username)
    if not userId:
        return "username not found"
    cipher = str(password) + str(userId)
    newCipher = str(newPassword) + str(userId)
    import hashlib
    hashedData = hashlib.sha256(cipher.encode())
    newHashedData = hashlib.sha256(newCipher.encode())
    if checkPassword(userId, hashedData):
        changePassword(userId, hashedData, newHashedData)
        return "password changed"
    else:
        return "invalid password"


# getting userId of username (returns None if not found)
def getUserId(username):
    fp = open("file1.txt", "r")
    dataLine = fp.readline()
    userId = None
    while(dataLine):
        uname = dataLine.split(",")[1]
        uname = uname.replace("\n", "")
        if uname == username:
            userId = dataLine.split(",")[0]
        dataLine = fp.readline()
    fp.close()
    return userId


# checking if password exist for userId
def checkPassword(userId, hashedData):
    fp = open("file2.txt", "r")
    string = str(userId) + "," + str(hashedData.hexdigest())
    dataLine = fp.readline()
    passwordFound = False
    while(dataLine):
        dataLine = dataLine.replace("\n", "")
        if dataLine == string:
            passwordFound = True
        dataLine = fp.readline()
    fp.close()
    return passwordFound


# code for changing the password
def changePassword(userId, hashedData, newHashedData):
    old = str(userId) + "," + str(hashedData.hexdigest())
    new = str(userId) + "," + str(newHashedData.hexdigest())
    with open("file2.txt", "r") as fp:
        lines = fp.readlines()
    with open("file2.txt", "w") as fp:
        for line in lines:
            if line.strip("\n") != old:
                fp.write(line)
        fp.write(new)


##############################################################################
@app.route('/newUser')
def newUser():
    return render_template('./newUser.html')


@app.route('/newUser', methods=['POST'])
def newUserPost():
    username = request.form['username']
    password = request.form['password']
    msg = addNewUserDriver(username, password)
    return msg


# Main driver function
def addNewUserDriver(username, password):
    if checkUsernameExists(username):
        return 'username already exists, try a new one'

    idExists = True
    while(idExists):
        userId = generateRandomId()
        # check if id already exists
        idExists = checkIdExists(userId)

    writeFile("file1.txt", userId, username)
    cipher = str(password) + str(userId)
    import hashlib
    hashedData = hashlib.sha256(cipher.encode())
    writeFile("file2.txt", userId, hashedData.hexdigest())
    return "New user added!"


# checking if usename exists in file1    
def checkUsernameExists(username):
    import os.path
    if not os.path.isfile("file1.txt"):
        fp = open("file1.txt", "w+")
        fp.close()
    fp = open("file1.txt", "r")

    dataLine = fp.readline()
    existsFlag = False
    while(dataLine):
        uname = dataLine.split(",")[1]
        uname = uname.replace("\n", "")
        if uname == username:
            existsFlag = True
        dataLine = fp.readline()
    fp.close()
    return existsFlag


# generating random userId
def generateRandomId():
    import random, string
    x = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(8))
    return x


# checking if userId already exists
def checkIdExists(userId):
    fp = open("file1.txt", "r")
    dataLine = fp.readline()
    existsFlag = False
    while(dataLine):
        uId = dataLine.split(",")[1]
        if uId == userId:
            existsFlag = True
        dataLine = fp.readline()
    fp.close()
    return existsFlag


# writing data in file
def writeFile(file, arg1, arg2):
    fp = open(file, "a")
    string = str(arg1) + "," + str(arg2) + "\n"
    fp.write(string)
    fp.close()
    
##############################################################################