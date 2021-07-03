from ml import *
import py_compile

path = os.path.dirname(__file__)
compiled = path + '\\compiled\\'

sys.path.append(path)

filters = ['assembler1.py', 'findbin.py']

def main():
    for py in os.listdir(path):
        if py == os.path.basename(__file__):
            continue

        if not py.endswith('.py'):
            continue

        if py.lower().find('.bin.py') != -1:
            continue

        if py.lower() in filters:
            continue

        print(py)

        py_compile.compile(py, compiled + os.path.splitext(py)[0] + '.pyc')

Try(main)

#input()