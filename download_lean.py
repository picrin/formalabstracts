import tarfile, subprocess, sys

lean_URL = "https://github.com/leanprover/lean/releases/download/v3.2.0/lean-3.2.0-linux.tar.gz"

import urllib.request
urllib.request.urlretrieve(lean_URL, lean_URL.split("/")[-1])


import tarfile
if (fname.endswith("tar.gz")):
    tar = tarfile.open(fname, "r:gz")
    tar.extractall()
    tar.close()
elif (fname.endswith("tar")):
    tar = tarfile.open(fname, "r:")
    tar.extractall()
    tar.close()

filename = "lean-3.2.0-linux.tar.gz"

tar = tarfile.open(filename, "r:gz")
tar.extractall()
tar.close()

exit = subprocess.run("lean-3.2.0-linux/bin/lean --make meta_data.lean", shell=True)

sys.exit(exit.returncode)
