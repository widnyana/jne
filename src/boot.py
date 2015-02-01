# -*- coding:utf-8 -*-
import argparse
import jne


def banner():
    print """                _   _                      _ _   _ ______
               | | | |                    | | \ | |  ____|
    _ __  _   _| |_| |__   ___  _ __      | |  \| | |__
   | '_ \| | | | __| '_ \ / _ \| '_ \ _   | | . ` |  __|
   | |_) | |_| | |_| | | | (_) | | | | |__| | |\  | |____
   | .__/ \__, |\__|_| |_|\___/|_| |_|\____/|_| \_|______|
   | |     __/ |
   |_|    |___/
                                        another Noisegate Labs stuff

,_._._._._._._._|____________________________________________________
|_|_|_|_|_|_|_|_|___________________________________________________/
                !
"""


class Dispatch(object):
    def __init__(self):
        self.message = "kopet"

    def run(self):
        print self.message


def dispatch(mode=None):
    """Dispatch action based on mode"""
    mode = "ini mode"
    print mode


def main():
    parser = argparse.ArgumentParser(
        description="Python JNE.\nInteract with JNE api via Python")
    parser.add_argument("-n", '--tracking-number', help="JNE.co.id Tracking Number", const=None)

    parser.add_argument('-f', '--of', help="Get City of Origin code", metavar="CITY NAME")
    parser.add_argument('-t', '--to', help="Get Shipping Destination Code", metavar="CITY NAME")

    group = parser.add_argument_group('group', "Get Pricelist.")
    group.add_argument('-o', '--origin', help="City of Origin", metavar="CITY CODE")
    group.add_argument('-d', '--destination', help="Shipping Destination", metavar="CITY CODE")
    group.add_argument('-w', '--weight', help="Package Weight, in KG", nargs="?", metavar="WEIGHT", const=int)

    parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')
    args = parser.parse_args()

    if args.tracking_number:
        jne.tracking(args.tracking_number)

    elif args.of:
        jne.get_from_code(args.of)

    elif args.to:
        jne.get_target_code(args.to)

    else:
        origin = args.origin
        dest = args.destination
        weight = args.weight

        if all([origin, dest, weight]):
            jne.checktariff(origin, dest, weight)

        else:
            parser.print_help()
