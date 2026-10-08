from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def as_dict(self):
        return {"id": self.id, "title": self.title, "created_at": self.created_at.isoformat()}
