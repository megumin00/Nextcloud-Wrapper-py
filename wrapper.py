#!/usr/bin/env python3
"""

    A program meant to wrap a client's simple HTTPS calls
    to the Nextcloud server.

    Requests documentation: https://docs.python-requests.org/en/master/api/

"""
import getpass, requests



class nc_wrapper:
    def __init__(self, nc_url, user_val, pass_val):
        self.base_url = nc_url
        self.basic_auth_headers = { "username":user_val, "password":pass_val }
        self.auth_tuple = ( user_val, pass_val )
    
    def download(self, suffix, filename):
        full_url = self.base_url + suffix + filename

        result = requests.request(method="GET", url=full_url, headers={"OCS-APIRequest": "true"}, auth=self.auth_tuple, timeout=60.0, verify=True)
        if (result.status_code == 200):
            output_f = open(filename, "wb")
            output_f.write(result.content)
            output_f.close()
        return result.reason

    def list(self, path):
        full_url = self.base_url+path
        
        result = requests.request(method="PROPFIND", url=full_url, auth=self.auth_tuple, timeout=60.0, verify=True)
        print(result.status_code)
        print(result.reason)
        print(result.content)
    
    def upload(self, dest_path, filename):
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

    # Now for the real test: try to LIST remote files, using WebDAV
    #if (server_link[-1] == "/"):
    #else:

    # List remote files in a server-side Documents directory
    #list_text = nc_wrapper.list("/remote.php/dav/files/"+user+"/Documents/")
    #print(list_text)
    
    # Download a remote file
    file_to_retrieve = "ale-video-slides---megumin-math-problem.odp"
    get_text = nc_wrapper.download("/remote.php/dav/files/"+user+"/Documents/", file_to_retrieve)
    print(get_text)

