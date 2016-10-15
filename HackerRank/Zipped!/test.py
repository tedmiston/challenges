"""
The stdin / stdout mocking is to avoid changing my code for every HackerRank
problem into requiring functions, besides one main function.  This approach,
as opposed to isolating reading input and printing output, and returning
values from a second function which is unit tested directly, allows the code
to be run both on the HackerRank app and locally with the only constraint
being the use of a main function locally.
"""

from io import StringIO
from unittest.mock import patch

from nose2.tools.params import params

from solution import main


def _load_input_file(filename):
    """Load the file with sample input, splitting the lines."""
    return open(filename).read().strip().split('\n')


def _load_output_file(filename):
    """Load the file with expected output for sample input."""
    return open(filename).read().strip()


@params(
    ('in.txt', 'out.txt'),
)
def test_zipped(input_filename, output_filename):
    """Test computing average grades by student.

    I've used side_effect instead of return_value on stdin because it accepts
    an iterable.
    """
    mock_in = _load_input_file(input_filename)
    expected = _load_output_file(output_filename)

    with patch('builtins.input', side_effect=mock_in), \
            patch('sys.stdout', new=StringIO()) as mock_out:
        main()
        actual = mock_out.getvalue().strip()
        assert actual == expected
