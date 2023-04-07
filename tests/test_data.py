"""Test data functionalities."""

from src.data.download import BundestagVoting


def test_bundestag_voting_class_init():
    """Test `BundestagVoting` class initialization."""
    bv = BundestagVoting()
    bv.browser.close()
    assert bv.url == (
        "https://www.bundestag.de/parlament/plenum/abstimmung/liste"
    )
