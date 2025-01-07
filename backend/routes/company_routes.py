from flask import Blueprint, jsonify
from http import HTTPStatus

company_blueprint = Blueprint('companies', __name__)

class CompanyController:
    def __init__(self, company_repository):
        self.company_repository = company_repository

    def register_routes(self, blueprint):
        blueprint.route('/')(self.get_all_companies)
        blueprint.route('/<int:company_id>')(self.get_company)

    def get_all_companies(self):
        companies = self.company_repository.get_all()
        return jsonify([{
            'id': c.id,
            'name': c.name,
            'industry': c.industry,
            'location': c.location
        } for c in companies]), HTTPStatus.OK

    def get_company(self, company_id):
        company = self.company_repository.get_by_id(company_id)
        if not company:
            return jsonify({'error': 'Company not found'}), HTTPStatus.NOT_FOUND
        
        return jsonify({
            'id': company.id,
            'name': company.name,
            'industry': company.industry,
            'location': company.location,
            'employees': [{
                'id': e.id,
                'name': e.name,
                'role': e.role
            } for e in company.employees],
            'performance': [{
                'quarter': p.quarter,
                'revenue': p.revenue,
                'profit_margin': p.profit_margin
            } for p in company.performance]
        }), HTTPStatus.OK
