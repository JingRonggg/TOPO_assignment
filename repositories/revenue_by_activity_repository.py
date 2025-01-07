from .base_repository import BaseRepository
from models import RevenueByActivity

class RevenueByActivityRepository(BaseRepository):
    def get_all(self):
        return RevenueByActivity.query.all()

    def get_by_id(self, id):
        return RevenueByActivity.query.get(id)

    def create(self, revenue):
        self.db.session.add(revenue)
        self.db.session.commit()
        return revenue

    def update(self, revenue):
        self.db.session.commit()
        return revenue

    def delete(self, revenue):
        self.db.session.delete(revenue)
        self.db.session.commit()