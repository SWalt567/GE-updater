import requests
import click

@click.command()
@click.argument('query_type', type=str)
def run(query_type):
    """GE-query script
    
    this script accesses the GE-proton git repo to either:
    a) return the tarball download link, or;
    b) return the name of the release

    Args:
        query_type (str): choose either "url" or "name" to get the respective data

    Returns:
        str: either the tarball download URL or the tarball filename
    """
    
    query_type.lower()
    # pass the query type into the main function
    query(query_type)


def get_data(data, query_type):
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

def query(query_type):
    # get the latest release information
    result = requests.get("https://api.github.com/repos/GloriousEggroll/proton-ge-custom/releases/latest").json()
    # initialize empty data str
    data = ""
    # find the specified data
    data = get_data(result["assets"], query_type)

    print(data)

run()