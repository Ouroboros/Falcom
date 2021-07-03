from ml import *
from importlib.machinery import SourceFileLoader

sys.dont_write_bytecode = True

def main():
    for path in sys.argv[1:]:
        os.chdir(os.path.abspath(path))
        for script in fileio.getDirectoryFiles(path, '*.py'):
            print(script)
            mod = SourceFileLoader(os.path.basename(script).split('.', 1)[0], script).load_module()

if __name__ == '__main__':
    Try(main)
