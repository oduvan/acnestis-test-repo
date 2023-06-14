from acnestis.processing import Processor
from acnestis.steps import concat_files

PROCESSOR = BaseProcessor([concat_files("poem.txt")], as_file="poem.txt")
