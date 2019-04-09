import os,wget


url = "https://files.rcsb.org/download/5a2g.pdb"  # Actual Code, The following one will not be valid code.
# url = "https://files.rcsb.org/download/1bdm.pdb" # Just for Try
file1 = wget.download(url, os.getcwd())