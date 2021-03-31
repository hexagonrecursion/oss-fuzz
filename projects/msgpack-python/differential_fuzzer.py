import sys


def TestOneInput(data):
  if data == b"hello":
    raise RuntimeError("world")


def main():
    import atheris
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
  main()
