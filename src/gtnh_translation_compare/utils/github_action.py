def set_output(name: str, value: str) -> None:
    """
    Set an output for a GitHub Action.

    Args:
        name: The name of the output.
        value: The value of the output.
    """
    print(f"::set-output name={name}::{value}")


def set_output_and_print(name: str, value: str) -> None:
    """
    Set an output for a GitHub Action and print it.

    Args:
        name: The name of the output.
        value: The value of the output.
    """
    set_output(name, value)
    print(f"{name}={value}")
