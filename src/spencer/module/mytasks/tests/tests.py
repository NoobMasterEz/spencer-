from unittest.mock import patch, Mock

from django.test import TestCase
from mytasks import tasks


class TestTasks(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    @patch("mytasks.tasks.add.run")
    def test_mock_task(mock_x, mock_y):
        tasks.add.run(1, 1).id
        assert tasks.add.run(1, 1)
        assert tasks.add.run.call_count == 2
        assert tasks.add.run.call_args.args == (1, 1)

    @patch("mytasks.tasks")
    def test_mock_task_return_value_side_effect(self, mock_task):
        mock_task.add.return_value = 1
        assert tasks.add(2, 2) == 4
        assert mock_task.add() == 1

    @patch("mytasks.tasks")
    def test_mock_task_raise_error_exceptions(self, mock_task):
        mock_task.add.side_effect = Mock(side_effect=Exception("Boom"))
        with self.assertRaises(Exception):
            mock_task.add()
