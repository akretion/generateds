#!/usr/bin/env python

#
# Generated  by generateDS.py.
#
# Command line options:
#   ('--no-dates', '')
#   ('--no-versions', '')
#   ('-p', 'tomato_')
#   ('--member-specs', 'list')
#   ('-f', '')
#   ('-o', 'tests/prefix_classname2_sup.py')
#   ('-s', 'tests/prefix_classname2_sub.py')
#   ('--super', 'prefix_classname2_sup')
#
# Command line arguments:
#   tests/prefix_classname.xsd
#
# Command line:
#   generateDS.py --no-dates --no-versions -p "tomato_" --member-specs="list" -f -o "tests/prefix_classname2_sup.py" -s "tests/prefix_classname2_sub.py" --super="prefix_classname2_sup" tests/prefix_classname.xsd
#
# Current working directory (os.getcwd()):
#   generateds
#

import sys

import prefix_classname2_sup as supermod

etree_ = None
Verbose_import_ = False
(
    XMLParser_import_none, XMLParser_import_lxml,
    XMLParser_import_elementtree
) = range(3)
XMLParser_import_library = None
try:
    # lxml
    from lxml import etree as etree_
    XMLParser_import_library = XMLParser_import_lxml
    if Verbose_import_:
        print("running with lxml.etree")
except ImportError:
    try:
        # cElementTree from Python 2.5+
        import xml.etree.cElementTree as etree_
        XMLParser_import_library = XMLParser_import_elementtree
        if Verbose_import_:
            print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # ElementTree from Python 2.5+
            import xml.etree.ElementTree as etree_
            XMLParser_import_library = XMLParser_import_elementtree
            if Verbose_import_:
                print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree_
                XMLParser_import_library = XMLParser_import_elementtree
                if Verbose_import_:
                    print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree_
                    XMLParser_import_library = XMLParser_import_elementtree
                    if Verbose_import_:
                        print("running with ElementTree")
                except ImportError:
                    raise ImportError(
                        "Failed to import ElementTree from any known place")


def parsexml_(*args, **kwargs):
    if (XMLParser_import_library == XMLParser_import_lxml and
            'parser' not in kwargs):
        # Use the lxml ElementTree compatible parser so that, e.g.,
        #   we ignore comments.
        kwargs['parser'] = etree_.ETCompatXMLParser()
    doc = etree_.parse(*args, **kwargs)
    return doc

#
# Globals
#

ExternalEncoding = 'ascii'

#
# Data representation classes
#


class tomato_peopleSub(supermod.tomato_people):
    def __init__(self, comments=None, person=None, programmer=None, python_programmer=None, java_programmer=None):
        super(tomato_peopleSub, self).__init__(comments, person, programmer, python_programmer, java_programmer, )
supermod.tomato_people.subclass = tomato_peopleSub
# end class tomato_peopleSub


class tomato_commentsSub(supermod.tomato_comments):
    def __init__(self, emp=None, valueOf_=None, mixedclass_=None, content_=None):
        super(tomato_commentsSub, self).__init__(emp, valueOf_, mixedclass_, content_, )
supermod.tomato_comments.subclass = tomato_commentsSub
# end class tomato_commentsSub


class tomato_personSub(supermod.tomato_person):
    def __init__(self, vegetable=None, fruit=None, ratio=None, id=None, value=None, name=None, interest=None, category=None, agent=None, promoter=None, description=None, extensiontype_=None):
        super(tomato_personSub, self).__init__(vegetable, fruit, ratio, id, value, name, interest, category, agent, promoter, description, extensiontype_, )
supermod.tomato_person.subclass = tomato_personSub
# end class tomato_personSub


class tomato_programmerSub(supermod.tomato_programmer):
    def __init__(self, vegetable=None, fruit=None, ratio=None, id=None, value=None, name=None, interest=None, category=None, agent=None, promoter=None, description=None, language=None, area=None, attrnegint=None, attrposint=None, attrnonnegint=None, attrnonposint=None, email=None, elposint=None, elnonposint=None, elnegint=None, elnonnegint=None, eldate=None, eldatetime=None, eltoken=None, elshort=None, ellong=None, elparam=None, elarraytypes=None, extensiontype_=None):
        super(tomato_programmerSub, self).__init__(vegetable, fruit, ratio, id, value, name, interest, category, agent, promoter, description, language, area, attrnegint, attrposint, attrnonnegint, attrnonposint, email, elposint, elnonposint, elnegint, elnonnegint, eldate, eldatetime, eltoken, elshort, ellong, elparam, elarraytypes, extensiontype_, )
supermod.tomato_programmer.subclass = tomato_programmerSub
# end class tomato_programmerSub


class tomato_paramSub(supermod.tomato_param):
    def __init__(self, semantic=None, name=None, flow=None, sid=None, type_=None, id=None, valueOf_=None):
        super(tomato_paramSub, self).__init__(semantic, name, flow, sid, type_, id, valueOf_, )
supermod.tomato_param.subclass = tomato_paramSub
# end class tomato_paramSub


class tomato_python_programmerSub(supermod.tomato_python_programmer):
    def __init__(self, vegetable=None, fruit=None, ratio=None, id=None, value=None, name=None, interest=None, category=None, agent=None, promoter=None, description=None, language=None, area=None, attrnegint=None, attrposint=None, attrnonnegint=None, attrnonposint=None, email=None, elposint=None, elnonposint=None, elnegint=None, elnonnegint=None, eldate=None, eldatetime=None, eltoken=None, elshort=None, ellong=None, elparam=None, elarraytypes=None, nick_name=None, favorite_editor=None):
        super(tomato_python_programmerSub, self).__init__(vegetable, fruit, ratio, id, value, name, interest, category, agent, promoter, description, language, area, attrnegint, attrposint, attrnonnegint, attrnonposint, email, elposint, elnonposint, elnegint, elnonnegint, eldate, eldatetime, eltoken, elshort, ellong, elparam, elarraytypes, nick_name, favorite_editor, )
supermod.tomato_python_programmer.subclass = tomato_python_programmerSub
# end class tomato_python_programmerSub


class tomato_java_programmerSub(supermod.tomato_java_programmer):
    def __init__(self, vegetable=None, fruit=None, ratio=None, id=None, value=None, name=None, interest=None, category=None, agent=None, promoter=None, description=None, language=None, area=None, attrnegint=None, attrposint=None, attrnonnegint=None, attrnonposint=None, email=None, elposint=None, elnonposint=None, elnegint=None, elnonnegint=None, eldate=None, eldatetime=None, eltoken=None, elshort=None, ellong=None, elparam=None, elarraytypes=None, status=None, nick_name=None, favorite_editor=None):
        super(tomato_java_programmerSub, self).__init__(vegetable, fruit, ratio, id, value, name, interest, category, agent, promoter, description, language, area, attrnegint, attrposint, attrnonnegint, attrnonposint, email, elposint, elnonposint, elnegint, elnonnegint, eldate, eldatetime, eltoken, elshort, ellong, elparam, elarraytypes, status, nick_name, favorite_editor, )
supermod.tomato_java_programmer.subclass = tomato_java_programmerSub
# end class tomato_java_programmerSub


class tomato_agentSub(supermod.tomato_agent):
    def __init__(self, firstname=None, lastname=None, priority=None, info=None):
        super(tomato_agentSub, self).__init__(firstname, lastname, priority, info, )
supermod.tomato_agent.subclass = tomato_agentSub
# end class tomato_agentSub


class tomato_special_agentSub(supermod.tomato_special_agent):
    def __init__(self, firstname=None, lastname=None, priority=None, info=None):
        super(tomato_special_agentSub, self).__init__(firstname, lastname, priority, info, )
supermod.tomato_special_agent.subclass = tomato_special_agentSub
# end class tomato_special_agentSub


class tomato_boosterSub(supermod.tomato_booster):
    def __init__(self, firstname=None, lastname=None, other_name=None, class_=None, other_value=None, type_=None, client_handler=None):
        super(tomato_boosterSub, self).__init__(firstname, lastname, other_name, class_, other_value, type_, client_handler, )
supermod.tomato_booster.subclass = tomato_boosterSub
# end class tomato_boosterSub


class tomato_infoSub(supermod.tomato_info):
    def __init__(self, rating=None, type_=None, name=None):
        super(tomato_infoSub, self).__init__(rating, type_, name, )
supermod.tomato_info.subclass = tomato_infoSub
# end class tomato_infoSub


class tomato_client_handlerTypeSub(supermod.tomato_client_handlerType):
    def __init__(self, fullname=None, refid=None):
        super(tomato_client_handlerTypeSub, self).__init__(fullname, refid, )
supermod.tomato_client_handlerType.subclass = tomato_client_handlerTypeSub
# end class tomato_client_handlerTypeSub


def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'people'
        rootClass = supermod.tomato_people
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
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'people'
        rootClass = supermod.tomato_people
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
    doc = parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'people'
        rootClass = supermod.tomato_people
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
    doc = parsexml_(inFilename)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'people'
        rootClass = supermod.tomato_people
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    if not silence:
        sys.stdout.write('#from prefix_classname2_sup import *\n\n')
        sys.stdout.write('import prefix_classname2_sup as model_\n\n')
        sys.stdout.write('rootObj = model_.rootClass(\n')
        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
        sys.stdout.write(')\n')
    return rootObj


USAGE_TEXT = """
Usage: python ???.py <infilename>
"""


def usage():
    print USAGE_TEXT
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
