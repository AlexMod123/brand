import pytest
import sys
from src.parse_cli import ParseArgs
def test_parse_args(monkeypatch):
    monkeypatch.setattr(
        sys, 'argv',
        ['script.py', '--files', 'a.csv', 'b.csv', '--report', 'average-rating']
    )
    args = ParseArgs()
    assert args.files == ['a.csv', 'b.csv']
    assert args.report == 'average-rating'

def test_parse_args_invalid_report(monkeypatch):
    monkeypatch.setattr(
        sys, 'argv',
        ['script.py', '--files', 'a.csv', '--report', 'invalid']
    )
    with pytest.raises(SystemExit):
        ParseArgs()