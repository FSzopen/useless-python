import hashlib
import optparse


def parse_args():
    """
    Computes MD5 digest for a file.
    """
    usage = """usage: %prog filepath"""
    parser = optparse.OptionParser(usage)
    options, args = parser.parse_args()
    return args


args = parse_args()


def md5sum(file, chunksize=65536):
    with open(file, "rb") as f:
        md5 = hashlib.md5()
        buffer = f.read(chunksize)
        while len(buffer):
            md5.update(buffer)
            buffer = f.read(chunksize)
    return md5.hexdigest()

for arg in args:
    try:
        print md5sum(arg), "           ", arg
    except IOError as e:
        print "%s: Not a file" %(arg)
