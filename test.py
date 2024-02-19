import pytest
from main import StudentsInMLOps

def test_enrollStudents():
    student = StudentsInMLOps()
    student.enrollStudents(5)
    assert student.getTotalStrength() == 5

def test_dropStudents():
    student = StudentsInMLOps()
    student.enrollStudents(10)
    student.dropStudents(3)
    assert student.getTotalStrength() == 7

def test_getClassName():
    student = StudentsInMLOps()
    assert student.getClassName() == "StudentsInMLOps"
