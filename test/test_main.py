import src.main

def test_add():
  assert src.main.add(1, 3) == 4
  assert src.main.add(1, -5) == -4
