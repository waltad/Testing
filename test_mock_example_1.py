import pytest

from mock_example_1 import BlogPostHistory
from unittest.mock import patch, MagicMock
from unittest import TestCase


class BlogPostHistoryTests(TestCase):

    def test_change_title(self):
        mock = MagicMock()

        with patch('mock_example_1.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')
            post_history.change_title("title2")
            assert post_history.get_properties() == ("title2", "desc")

    def test_change_desc(self):
        mock = MagicMock()

        with patch('mock_example_1.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')
            post_history.change_description("desc2")
            assert post_history.get_properties() == ("title", "desc2")

    def test_problem_with_file(self):
        mock = MagicMock(side_effect=OSError)

        with patch('mock_example_1.BlogPostHistory.save', mock):
            post_history = BlogPostHistory('title', 'desc')
            with pytest.raises(Exception):
                post_history.change_description("desc2")


