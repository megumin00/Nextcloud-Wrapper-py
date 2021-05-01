#!/usr/bin/env python3
"""

    A program meant to wrap a client's simple HTTPS calls
    to the Nextcloud server.

    Requests documentation: https://docs.python-requests.org/en/master/api/
    
    This test actually demonstrates how the python requests API will NOT be
    sufficient for accessing files using webDAV urls.

    An example execution I/O excerpt is:
    ```
    server name: https://www.example.com/nextcloud
    username: chozorho
    Password:
    Now trying https://www.example.com/nextcloud/remote.php/dav/files/chozorho/Documents/
    b'This is the WebDAV interface. It can only be accessed by WebDAV clients such as the Nextcloud desktop sync client.'
    ```

    So we'll need to use a different API.

"""
import getpass, requests



class nc_wrapper:
    def __init__(self, nc_url, user_val, pass_val):
        self.base_url = nc_url
        self.basic_auth_headers = { "username":user_val, "password":pass_val }
        self.auth_tuple = ( user_val, pass_val )
    
    def download(self, suffix):
        full_url = self.base_url+suffix
        print("Now trying %s" % full_url)

        result = requests.request(method="GET", url=full_url, auth=self.auth_tuple, timeout=60.0, verify=True)
        if (result.status_code == 200):
            return result.content
        else:
            return result.reason
    
    def upload(self, filename, destination):
        all_headers = {}
        full_url = self.base_url+suffix
        #result = requests.request(method="POST", url=full_url, headers=, timeout=60.0, verify=True)
        pass
    
if __name__ == '__main__':
    # TODO ensure that this authentication strategy
    # truly is secure (and doesn't leak any passwords)!
    # Sooner or later, I can use Wireshark to do this.

    # Get user input for the actual arguments
    server_link = input("server name: ")
    user = input("username: ")
    passwd = getpass.getpass()
    nc_wrapper = nc_wrapper(server_link, user, passwd)

    # Now for the real test: try a GET request using WebDAV!
    #if (server_link[-1] == "/"):
    #else:
    get_text = nc_wrapper.download("/remote.php/dav/files/"+user+"/Documents/")
    print(get_text)

