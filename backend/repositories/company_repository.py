from .base_repository import BaseRepository
from ..models import Company

class CompanyRepository(BaseRepository):
    def get_all(self):
        return Company.query.all()

    def get_by_id(self, id):
        return Company.query.get(id)

    def create(self, company):
        self.db.session.add(company)
        self.db.session.commit()
        return company

    def update(self, company):
        self.db.session.commit()
        return company

    def delete(self, company):
        self.db.session.delete(company)
        self.db.session.commit()

    def get_by_industry(self, industry):
        return Company.query.filter_by(industry=industry).all()
