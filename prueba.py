import pytest

def inc(x):
    return x + 1


class TestFileloader:   
  def testthis(self):
    status  = inc(4)
    assert status == 5
