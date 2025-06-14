# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "benfords-sawzall",
# ]
#
# [tool.uv.sources]
# benfords-sawzall = { path = "." }
# ///

import benfords_sawzall as bz


def main() -> None:
    print(bz.hello())


if __name__ == "__main__":
    main()
