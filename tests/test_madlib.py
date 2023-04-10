from madlib_cli.madlib import open_file
import pytest
def test_one():
    actual=open_file()
    exteted="It was a {Adjective} and {Adjective} {Noun}."
    assert actual==exteted