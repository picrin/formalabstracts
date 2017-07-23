import tarfile, subprocess, sys

filename = "lean-3.2.0-linux.tar.gz"

tar = tarfile.open(filename, "r:gz")
tar.extractall()
tar.close()

exit = subprocess.run("lean-3.2.0-linux/bin/lean --make meta_data.lean", shell=True)

sys.exit(exit.returncode)
