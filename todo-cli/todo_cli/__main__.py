import pkg_resources
from .args import args
from .models import My_funtions
import json
def main():
    obj = My_funtions()
    r = ""
    if args.desc and args.add:
        r = obj.add(args.add, args.desc)
    elif args.add:
        r = obj.add(args.add)
    elif args.done:
        r = obj.done(args.done)
    elif args.show:
        r = obj.show(args.show)
    elif args.tasks:
        r = obj.tasks_status(0)
    elif args.all:
        r = obj.all()
    elif args.completed:
        r = obj.tasks_status(1)
    else:
        print("Please use --help flag")
    if (r and r.status_code == 200):
        print(json.dumps(json.loads(r.content), indent=4, sort_keys=True))
    elif (r and r.status_code == 404):
            print("Result not found!")

if __name__ == '__main__':
    main()
