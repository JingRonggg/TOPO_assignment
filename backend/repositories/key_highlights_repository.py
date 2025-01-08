from .base_repository import BaseRepository
from ..models import KeyHighlights

class KeyHighlightsRepository(BaseRepository):
    def get_all(self):
        return KeyHighlights.query.all()

    def get_by_id(self, id):
        return KeyHighlights.query.get(id)

    def create(self, key_highlight):
        self.db.session.add(key_highlight)
        self.db.session.commit()
        return key_highlight

    def update(self, key_highlight):
        self.db.session.commit()
        return key_highlight

    def delete(self, key_highlight):
        self.db.session.delete(key_highlight)
        self.db.session.commit() 