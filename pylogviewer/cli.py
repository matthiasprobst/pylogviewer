import argparse

from .core import start


def main():
    """main command line interface function"""
    parser = argparse.ArgumentParser(description='PyLogViewer command line interface')
    start()
