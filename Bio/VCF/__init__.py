#!/usr/bin/env python
"""
A VCFv4.0 and 4.1 parser for Python.

Online version of PyVCF documentation is available at http://pyvcf.rtfd.org/
"""


from Bio.VCF.parser import Reader, Writer
from Bio.VCF.parser import VCFReader, VCFWriter
from Bio.VCF.filters import Base as Filter
from Bio.VCF.parser import RESERVED_INFO, RESERVED_FORMAT
from Bio.VCF.sample_filter import SampleFilter
from Bio.VCF.utils import walk_together, trim_common_suffix
from Bio.VCF.phase import PhasedReader, PhasedWriter

VERSION = '0.0.1'
