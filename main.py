# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "benfords-sawzall",
# ]
#
# [tool.uv.sources]
# benfords-sawzall = { path = ".", editable = true }
# ///

import code
import benfords_sawzall as bz
from benfords_sawzall import *


def main() -> None:
    print(bz.hello())

    code.interact(local=globals())


if __name__ == "__main__":
    main()
