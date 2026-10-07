import pytest

from tasktrack import remove_task_by_number


def test_remove_first_task():
    tasks = ["Task 1", "Task 2", "Task 3"]

    removed = remove_task_by_number(tasks, 1)

    assert removed == "Task 1"
    assert tasks == ["Task 2", "Task 3"]


def test_remove_middle_task():
    tasks = ["Task 1", "Task 2", "Task 3"]

    removed = remove_task_by_number(tasks, 2)

    assert removed == "Task 2"
    assert tasks == ["Task 1", "Task 3"]

def test_remove_last_task():
    tasks = ["Task 1", "Task 2", "Task 3"]

    removed = remove_task_by_number(tasks, 3)

    assert removed == "Task 3"
    assert tasks == ["Task 1", "Task 2"]

def test_remove_zero():
    tasks = ["Task 1", "Task 2", "Task 3"]

    removed = remove_task_by_number(tasks, 0)

    assert removed is None
    assert tasks == ["Task 1", "Task 2", "Task 3"]

def test_remove_too_large_number():
    tasks = ["Task 1", "Task 2", "Task 3"]

    removed = remove_task_by_number(tasks, 4)

    assert removed is None
    assert tasks == ["Task 1", "Task 2", "Task 3"]

def test_remove_negative_number():
    tasks = ["Task 1", "Task 2", "Task 3"]

    removed = remove_task_by_number(tasks, -1)

    assert removed is None
    assert tasks == ["Task 1", "Task 2", "Task 3"]