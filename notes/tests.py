from django.test import TestCase

from notes.models import Note


class NoteModelTests(TestCase):
    def test_as_dict_round_trips_title(self):
        note = Note.objects.create(title="hello bazelcon")

        self.assertEqual(note.as_dict()["title"], "hello bazelcon")
        self.assertEqual(Note.objects.count(), 1)
