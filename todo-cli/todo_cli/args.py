import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-a','--add', help='Add a task to todo list')
parser.add_argument('-d','--done', help='Change the status of task to done. Provide task id', type=int)
parser.add_argument('-s','--show', help='Show detail of a particular task. Provide task id', type=int)
parser.add_argument('-t','--tasks', help='Show all pending tasks', action='store_true')
parser.add_argument('--all', help='Show all tasks', action='store_true')
parser.add_argument('--completed', help='Show all complted tasks', action='store_true')
parser.add_argument('--desc', help='Can be used with -a or -add argument to add description to a task')
args = parser.parse_args()

# args.b will be None if b is not provided

if (getattr(args,"desc") and not (getattr(args,"add"))):
    sys.exit("Cannot supply --desc without -add")
