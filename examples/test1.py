import sys
import time

from python_claml import claml
from python_claml.claml_types import ClaML


def to_string(nodes):
    """
    Serialise a forest of DOM nodes to text,
    using the data fields of text nodes.
    :param nodes: the forest of DOM nodes
    :return: a concatenation of string representations.
    """
    result = []
    for node in nodes:
        if node.nodeType == node.TEXT_NODE:
            result.append(node.data)
        else:
            result.append(to_string(node.childNodes))
    return ''.join(result)


def parse_file(file_name: str) -> ClaML:
    """
    Parse a ClaML file and write one line per Class read
    :param file_name: the input file name
    """
    with open(file_name, 'r') as input_file:
        print('Reading file contents from {} ...'.format(file_name), file=sys.stderr)
        start = time.perf_counter()
        contents = input_file.read()
        mid = time.perf_counter()
        print('Parsing ClaML document ...', file=sys.stderr)
        classification: ClaML = claml.CreateFromDocument(contents)
        end = time.perf_counter()
        print('Took {:f}s, reading: {:f}s, parsing: {:f}s\n'.format(
            end - start,
            mid - start,
            end - mid
        ), file=sys.stderr)
        for classKind in classification.ClassKinds.ClassKind:
            print('ClassKind: {}'.format(classKind.name))
        for cls in classification.Class:
            for superClass in cls.SuperClass:
                for rubric in cls.Rubric:
                    if rubric.kind == 'preferred':
                        for label in rubric.Label:
                            nodes = label.toDOM().childNodes
                            print('Class {} ({}) [{}] {}'.format(
                                cls.code,
                                cls.kind,
                                superClass.code,
                                'Label: ' + to_string(nodes)
                            ))
        return classification


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <input.xml>'.format(sys.argv[0]), file=sys.stderr)
        exit(1)
    result = parse_file(sys.argv[1])
