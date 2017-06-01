#!/usr/bin/env python

"""
usage: show_schema_hierarchy.py [-h] [-i INDENT] [--eliminate-branch-dups]
                                [--show-loop-references] [-v]
                                inschema

synopsis:
  show an indented schema hierarchy of xs:include/xs:import.

positional arguments:
  inschema              The input (root) schema

optional arguments:
  -h, --help            show this help message and exit
  -i INDENT, --indent INDENT
                        Indent string. default: " " (4 spaces)
  --eliminate-branch-dups
                        Eliminate (ignore) duplicate references even when
                        previously seen in other branches
  --show-loop-references
                        Show references that would cause loops
  -v, --verbose         Print messages during actions.

examples:
  python show_schema_hierarchy.py root_schema.xsd
"""


#
# imports
from __future__ import print_function
#import sys
import argparse
from lxml import etree


#
# Global variables


#
# Private functions

def dbg_msg(options, msg):
    """Print a message if verbose is on."""
    if options.verbose:
        print(msg)


#
# Exported functions


def show_hierarchy(inschema, path, indent, namespaces, previous, options):
    if not inschema.startswith('http') and path:
        inschemaloc = '{}/{}'.format(path, inschema)
    else:
        inschemaloc = inschema
    if inschema in previous:
        if options.show_loop_references:
            print('{}*loop* -- {}'.format(indent, inschemaloc))
        #print('{} *previous* -- {}'.format(indent, previous))
        return
    previous.add(inschema)
    print('{}{} -- {}'.format(indent, inschema, inschemaloc))
    doc = etree.parse(inschemaloc)
    root = doc.getroot()
    elements = root.xpath('./xs:include', namespaces=namespaces)
    elements += root.xpath('./xs:import', namespaces=namespaces)
    indent1 = indent + options.indent
    if inschema.startswith('http'):
        stem = inschema.split('/')[-1]
        ln = 0 - (len(stem) + 1)
        path = inschema[:ln]
    for element in elements:
        location = element.get('schemaLocation')
        if options.eliminate_branch_dups:
            previous1 = previous
        else:
            previous1 = previous.copy()
        show_hierarchy(location, path, indent1, namespaces, previous1, options)


def main():
    description = """\
synopsis:
  show an indented schema hierarchy of schema documents that are
  pulled in by xs:include and xs:import.
"""
    epilog = """\
examples:
  python show_schema_hierarchy.py root_schema.xsd
  python show_schema_hierarchy.py -v --show-loop-references root_schema.xsd
"""
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "inschema",
        help="the input (root) schema",
    )
    parser.add_argument(
        "-i", "--indent",
        default="    ",
        help='indent string. default is 4 spaces',
    )
    parser.add_argument(
        "--eliminate-branch-dups",
        action="store_true",
        help="eliminate (ignore) duplicate references even when previously "
             "seen in other branches",
    )
    parser.add_argument(
        "--show-loop-references",
        action="store_true",
        help="show references that would cause loops"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="print additional messages during actions.",
    )
    options = parser.parse_args()
    parent = ''
    indent = ''
    namespaces = {'xs': 'http://www.w3.org/2001/XMLSchema'}
    previous = set()
    show_hierarchy(
        options.inschema, parent, indent, namespaces, previous, options)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    #import ipdb; ipdb.set_trace()
    main()
