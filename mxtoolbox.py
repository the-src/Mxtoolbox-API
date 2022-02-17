import argparse
from os import environ
from dotenv import load_dotenv
from mt.mxtoolbox import mxtoolbox as mt

load_dotenv()

parser = argparse.ArgumentParser(
    usage="mxtoolbox.py (-a [action]) (-l [lookup])", description="Checks whether your mail servers are blacklisted using Mxtoolbox REST API")
parser.add_argument('-a', metavar='', type=str, nargs=1,
                    help='pick one action: monitor, usage. For lookup use "-l"')
parser.add_argument('-r', action='store_true',
                    help='use for raw input')
parser.add_argument('-l', metavar=' lookup', type=str, nargs=1,
                    help='Give lookup type: smtp, mx, ...(https://mxtoolbox.com/SuperTool.aspx)')

args = parser.parse_args()

if not (args.a or args.l):
    parser.error('No action requested, add -a or -l')

API = mt(key=environ.get('ENV'))

if args.l and args.r:
    stool = input('What do you want to lookup?\n>> ')
    print(API.lookup(command=args.l[0], argument=stool, RAW=True))
    quit()
elif args.l:
    stool = input('What do you want to lookup?\n>> ')
    print(API.lookup(command=args.l[0], argument=stool))
    quit()

run = getattr(API, args.a[0])

if args.a and args.r:
    print(run(RAW=True))
    quit()
elif args.a:
    print(run())
