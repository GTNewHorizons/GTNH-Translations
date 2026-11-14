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


def write_summary(markdown: str) -> None:
    """Append markdown to the job summary shown on the run page; does nothing outside GitHub Actions."""
    if "GITHUB_STEP_SUMMARY" in os.environ:
        with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as fp:
            fp.write(markdown)


def set_output_and_print(name: str, value: str) -> None:
    """
    Set an output for a GitHub Action and print it.

    Args:
        name: The name of the output.
        value: The value of the output.
    """
    set_output(name, value)
    print(f"{name}={value}")
