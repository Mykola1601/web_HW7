
from pprint import pprint
import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError
from crud import create, read, update, delete

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--action")
parser.add_argument("-m", "--model")
parser.add_argument("-n", "--name")
parser.add_argument("-id", "--id")

args = parser.parse_args()

action = args.action
model = args.model
name = args.name
id = args.id

def main():
    match action:
        case "create":
            create(model, name, id)
        case "list":
            return(read(model, name, id))
        case "update":
            return(update(model, name, id))
        case "remove":
            return(delete(model, name, id))
        case _:
            return "nothing parse"

if __name__ == '__main__':
    pprint (main())


'''
--action create -m Teacher --name 'Boris Jonson' створення вчителя
--action list -m Teacher показати всіх вчителів
--action update -m Teacher --id 3 --name 'Andry Bezos' оновити дані вчителя з id=3
--action remove -m Teacher --id 3 вида
 py main.py -a create -m Teacher -n 'Boris Jonson'
'''




