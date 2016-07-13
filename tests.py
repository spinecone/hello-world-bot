import unittest
from bot import get_next_chunk
import book_manager
import tempfile
import os
from unittest.mock import patch

class TestBot(unittest.TestCase):

  def test_get_next_chunk_returns_short_sentences(self):
    test_book = "this is the first line. this is the second line."
    test_file = tempfile.NamedTemporaryFile('r+', delete = False)
    test_file.write(test_book)
    test_file.close()
    with patch('book_manager.book_file', test_file.name):
      message = get_next_chunk()
      self.assertEqual(message, "this is the first line.")
    os.remove(test_file.name)

  def test_get_next_chunk_returns_segments_of_long_sentences(self):
    test_book = "this is the first line which is rather long and won't fit within the limits of a single tweet so we'll have to truncate it a little bit unfortunately. this is the second line."
    test_file = tempfile.NamedTemporaryFile('r+', delete = False)
    test_file.write(test_book)
    test_file.close()
    with patch('book_manager.book_file', test_file.name):
      message = get_next_chunk()
      self.assertEqual(message, "this is the first line which is rather long and won't fit within the limits of a single tweet so we'll have to truncate it a little bit unfo")
    os.remove(test_file.name)

  def test_get_next_chunk_deletes_message_from_book(self):
    test_book = "this is the first line. this is the second line."
    test_file = tempfile.NamedTemporaryFile('r+', delete = False)
    test_file.write(test_book)
    test_file.close()
    with patch('book_manager.book_file', test_file.name):
      message = get_next_chunk()
    new_contents = open(test_file.name, 'r+')
    self.assertEqual(new_contents.read(), ' this is the second line.')
    new_contents.close()
    os.remove(test_file.name)

if __name__ == '__main__':
  unittest.main()
