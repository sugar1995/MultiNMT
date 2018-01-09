"""Train model."""

from nmt import nmt

import tensorflow as tf
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    nmt.add_arguments(parser)
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=nmt.main, argv=[sys.argv[0]] + unparsed)
