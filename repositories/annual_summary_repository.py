from .base_repository import BaseRepository
from models import AnnualSummary

class AnnualSummaryRepository(BaseRepository):
    def get_all(self):
        return AnnualSummary.query.all()

    def get_by_id(self, id):
        return AnnualSummary.query.get(id)

    def create(self, summary):
        self.db.session.add(summary)
        self.db.session.commit()
        return summary

    def update(self, summary):
        self.db.session.commit()
        return summary

    def delete(self, summary):
        self.db.session.delete(summary)
        self.db.session.commit()