from .base_repository import BaseRepository
from ..models import RevenueDistribution

class RevenueDistributionRepository(BaseRepository):
    def get_all(self):
        return RevenueDistribution.query.all()

    def get_by_id(self, id):
        return RevenueDistribution.query.get(id)

    def create(self, RevenueDistribution):
        self.db.session.add(RevenueDistribution)
        self.db.session.commit()
        return RevenueDistribution

    def update(self, RevenueDistribution):
        self.db.session.commit()
        return RevenueDistribution

    def delete(self, RevenueDistribution):
        self.db.session.delete(RevenueDistribution)
        self.db.session.commit() 