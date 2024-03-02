import os


def set_output(name: str, value: str) -> None:
    """
    Set an output for a GitHub Action.

    Args:
        name: The name of the output.
        value: The value of the output.
    """
    # echo "{name}={value}" >> $GITHUB_OUTPUT
    if "GITHUB_OUTPUT" in os.environ:
        with open(os.environ["GITHUB_OUTPUT"], "a") as fp:
            fp.write(f"{name}={value}\n")


def set_output_and_print(name: str, value: str) -> None:
    """
    Set an output for a GitHub Action and print it.

    Args:
        name: The name of the output.
        value: The value of the output.
    """
    set_output(name, value)
    print(f"{name}={value}")
