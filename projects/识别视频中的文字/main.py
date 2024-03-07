import argparse


Class MainCommand()

parser = argparse.ArgumentParser()
parser.add_argument('--x', required=True, help='foo help')
parser.add_argument('--foox', help='foo helpx')

args = parser.parse_args()