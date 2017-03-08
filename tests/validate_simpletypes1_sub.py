#!/usr/bin/env python

#
# Generated  by generateDS.py.
#
# Command line options:
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('--member-specs', 'list')
#   ('-f', '')
#   ('-o', 'tests/validate_simpletypes2_sup.py')
#   ('-s', 'tests/validate_simpletypes2_sub.py')
#   ('--super', 'validate_simpletypes2_sup')
#
# Command line arguments:
#   tests/validate_simpletypes.xsd
#
# Command line:
#   generateDS.py --no-dates --no-versions --member-specs="list" -f -o "tests/validate_simpletypes2_sup.py" -s "tests/validate_simpletypes2_sub.py" --super="validate_simpletypes2_sup" tests/validate_simpletypes.xsd
#
# Current working directory (os.getcwd()):
#   generateds
#

import sys
from lxml import etree as etree_

import validate_simpletypes2_sup as supermod

def parsexml_(infile, parser=None, **kwargs):
    if parser is None:
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        parser = etree_.ETCompatXMLParser()
    doc = etree_.parse(infile, parser=parser, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class containerTypeSub(supermod.containerType):
    def __init__(self, sample1=None, sample2_bad=None, sample3_bad=None, sample4_bad=None, sample2=None):
        super(containerTypeSub, self).__init__(sample1, sample2_bad, sample3_bad, sample4_bad, sample2, )
supermod.containerType.subclass = containerTypeSub
# end class containerTypeSub


class simpleOneTypeSub(supermod.simpleOneType):
    def __init__(self, integer_range_1_value=None, pattern_value=None, token_enum_value=None, integer_range_incl_value=None, integer_range_excl_value=None, min_max_length_value=None, length_value=None, totalDigits_value=None, date_minincl_value=None, date_maxincl_value=None, date_minexcl_value=None, date_maxexcl_value=None, time_minincl_value=None, time_maxincl_value=None, time_minexcl_value=None, time_maxexcl_value=None, datetime_minincl_value=None, datetime_maxincl_value=None, datetime_minexcl_value=None, datetime_maxexcl_value=None, vbar_pattern_value=None, anonymous_float_value=None, primative_integer=None, primative_float=None):
        super(simpleOneTypeSub, self).__init__(integer_range_1_value, pattern_value, token_enum_value, integer_range_incl_value, integer_range_excl_value, min_max_length_value, length_value, totalDigits_value, date_minincl_value, date_maxincl_value, date_minexcl_value, date_maxexcl_value, time_minincl_value, time_maxincl_value, time_minexcl_value, time_maxexcl_value, datetime_minincl_value, datetime_maxincl_value, datetime_minexcl_value, datetime_maxexcl_value, vbar_pattern_value, anonymous_float_value, primative_integer, primative_float, )
supermod.simpleOneType.subclass = simpleOneTypeSub
# end class simpleOneTypeSub


class simpleTwoTypeSub(supermod.simpleTwoType):
    def __init__(self, simpleTwoElementOne=None):
        super(simpleTwoTypeSub, self).__init__(simpleTwoElementOne, )
supermod.simpleTwoType.subclass = simpleTwoTypeSub
# end class simpleTwoTypeSub


class simpleTwoElementOneTypeSub(supermod.simpleTwoElementOneType):
    def __init__(self, simpleTwoElementTwo=None):
        super(simpleTwoElementOneTypeSub, self).__init__(simpleTwoElementTwo, )
supermod.simpleTwoElementOneType.subclass = simpleTwoElementOneTypeSub
# end class simpleTwoElementOneTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'containerType'
        rootClass = supermod.containerType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='',
            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'containerType'
        rootClass = supermod.containerType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    if not silence:
        content = etree_.tostring(
            rootElement, pretty_print=True,
            xml_declaration=True, encoding="utf-8")
        sys.stdout.write(content)
        sys.stdout.write('\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    from StringIO import StringIO
    parser = None
    doc = parsexml_(StringIO(inString), parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'containerType'
        rootClass = supermod.containerType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('<?xml version="1.0" ?>\n')
        rootObj.export(
            sys.stdout, 0, name_=rootTag,
            namespacedef_='')
    return rootObj


def parseLiteral(inFilename, silence=False):
    parser = None
    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'containerType'
        rootClass = supermod.containerType
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from validate_simpletypes2_sup import *\n\n')
        sys.stdout.write('import validate_simpletypes2_sup as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
