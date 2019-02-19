import os
path = os.path.dirname(os.path.abspath(__file__))
os.system("echo alias todo=\\'python3 {0}/main.py\\' >> "
          "~/.bash_aliases".format(path))
os.system("bash")
