import sys
import os

# Add the install directory to the system path
install_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'install/lib/python3.10/site-packages'))
sys.path.insert(0, install_path)

from hello import hello

def main():
    print(hello("world"))

if __name__ == "__main__":
    main()
