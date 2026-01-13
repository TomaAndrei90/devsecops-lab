import subprocess
import sys

comanda_utilizator = sys.argv[1]
subprocess.call(comanda_utilizator, shell=True)
