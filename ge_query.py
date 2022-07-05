import requests
import click
import os

@click.command()
@click.argument('query_type', type=str)
def run(query_type):
    """GE-query script
    
    this script accesses the GE-proton git repo to either:
    a) return the tarball download link, or;
    b) return the name of the release, or;
    c) check if the update is already installed

    Args:
        query_type (str): choose either "url" or "name" to 
        get the respective data, or "check" to check if the 
        update is already installed

    Returns:
        str: either the tarball download URL or the tarball filename
    """
    
    # filter user input
    query_type = str(query_type).lower()
    
    # pass the query type into the main function
    query(query_type)

def get_data(data, query_type):
    """ Data filtering function

    Args:
        data (dict): the data to filter through
        query_type (str): the type of data to look for

    Returns:
        str: returns the desired data
    """
    
    asset = None
    # iterate over assets
    for asset in data:
        # check each asset
        if asset["browser_download_url"][-6:] == "tar.gz":
            # if the file is ".tar.gz" its the right one
            
            # return either the URL or name depending on the user's selection
            if query_type == "url":
                return asset["browser_download_url"]
            if query_type == "name":
                return asset["name"]              
    # return nothing if the tar can't be found
    return None

def can_update(data):
    """ Release check
    
    Compares the newest release with what is currently installed in
    order to avoid downloading the same update twice

    Args:
        data (dir): the data of the current release
        
    Returns:
        True if already up-to-date, else false
    """
    
    # get the current GE-proton version
    current = get_data(data, "name")
    # get the path to .steam/root/compatibilitytools.d/
    path = os.path.expanduser("~/.steam/root/compatibilitytools.d/")
    versions = os.listdir(path)
    
    return False if current[:-7] in versions else True

def query(query_type):
    """ the main function

    Args:
        query_type (str): the type of data to look for
    """
    
    # get the latest release information
    result = requests.get("https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest").json()
    # make an assets dir, this will contain all of the latest release information
    assets = result["assets"]
    
    if query_type == "check":
        print(can_update(assets))
    else:
        print(get_data(assets, query_type))

run()