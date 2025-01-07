from datetime import datetime
from models import Company, Employee, CompanyPerformance
from sqlalchemy.exc import IntegrityError

class DataLoaderService:
    def __init__(self, company_repository, db):
        self.company_repository = company_repository
        self.db = db

    def load_json_data(self, data):
        try:
            self._clear_existing_data()
            
            if not isinstance(data, dict) or 'companies' not in data:
                raise ValueError("Invalid data format: Expected dict with 'companies' key")

            for company_data in data['companies']:
                company = self._create_company(company_data)
                if 'employees' in company_data:
                    self._create_employees(company_data['employees'], company.id)
                if 'performance' in company_data:
                    self._create_performance_data(company_data['performance'], company.id)
            
            self.db.session.commit()
            return True
        except Exception as e:
            self.db.session.rollback()
            raise e

    def _clear_existing_data(self):
        try:
            CompanyPerformance.query.delete()
            Employee.query.delete()
            Company.query.delete()
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            raise

    def _create_company(self, company_data):
        try:
            company = Company(
                id=company_data.get('id'),
                name=company_data.get('name'),
                industry=company_data.get('industry'),
                revenue=company_data.get('revenue'),
                location=company_data.get('location')
            )
            self.db.session.add(company)
            self.db.session.flush()
            return company
        except KeyError as e:
            raise ValueError(f"Missing required company field: {str(e)}")

    def _create_employees(self, employees_data, company_id):
        for emp_data in employees_data:
            try:
                hired_date = None
                if emp_data.get('hired_date'):
                    hired_date = datetime.strptime(emp_data['hired_date'], '%Y-%m-%d').date()
                
                employee = Employee(
                    id=emp_data.get('id'),
                    name=emp_data.get('name'),
                    role=emp_data.get('role'),
                    salary=emp_data.get('salary'),
                    hired_date=hired_date,
                    company_id=company_id
                )
                self.db.session.add(employee)
            except KeyError as e:
                raise ValueError(f"Missing required employee field: {str(e)}")

    def _create_performance_data(self, performance_data, company_id):
        for quarter, perf_data in performance_data.items():
            try:
                performance = CompanyPerformance(
                    company_id=company_id,
                    quarter=quarter,
                    revenue=perf_data.get('revenue'),
                    profit_margin=perf_data.get('profit_margin')
                )
                self.db.session.add(performance)
            except KeyError as e:
                raise ValueError(f"Missing required performance field: {str(e)}")
