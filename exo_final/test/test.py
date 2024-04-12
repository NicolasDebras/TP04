import pytest
from models.note import Note
from service.utils import getNewId,removeTask
from datetime import datetime


def test_check_if_done():
    listNote = []
    note = Note(getNewId(listNote), "test")
    note.check_note()
    assert note.isChecked


def test_check_if_create_correct_content():
    listNote = []
    note = Note(getNewId(listNote), "test")
    note.check_note()
    assert note.content == "test"


def test_check_if_remove_correct_content():
    listNote = []
    listNote.append(Note(12, "test"))
    listNote.append(Note(36, "new"))
    note =removeTask(12,listNote)
    assert note[0].id!=12
