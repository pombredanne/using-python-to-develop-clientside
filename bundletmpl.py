import json

import os

def accumulate():
    accumulated = {}
    for dirname, _, fnames in os.walk('tmpls'):
        for fname in fnames:
            fp = open(os.path.join(dirname, fname), 'r')
            accumulated[fname] = fp.read()
            fp.close()
            pass
        pass
    return json.dumps(accumulated)

def main():
    a = accumulate()
    j = """
    module.exports = {a};
    """.strip().format(a=a)
    fp = open('src/tmpl.js', 'w')
    fp.write(j)
    fp.close()
    pass

if __name__ == '__main__':
    main()
