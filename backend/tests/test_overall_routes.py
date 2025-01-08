import pytest
from flask import Flask, Blueprint
from unittest.mock import Mock, patch
from datetime import datetime

from backend.routes.overall_routes import OverallController, overall_blueprint
from backend.models import Company, Employee, CompanyPerformance, MemberActivity, QuarterlyPerformance

@pytest.fixture
def mock_repositories():
    # Mock company data
    mock_employee = Mock()
    mock_employee.id = 1
    mock_employee.name = "John Doe"
    mock_employee.role = "Developer"
    
    mock_company_performance = Mock()
    mock_company_performance.profit_margin = 0.25
    mock_company_performance.quarter = "Q1"
    mock_company_performance.revenue = 100000
    
    mock_company = Mock()
    mock_company.id = 1
    mock_company.name = "Test"
    mock_company.industry = "Tech"
    mock_company.location = "NYC"
    mock_company.employees = [mock_employee]
    mock_company.performance = [mock_company_performance]

    # Mock activity data
    mock_activity = Mock()
    mock_activity.id = 1
    mock_activity.date = datetime(2024, 1, 1)
    mock_activity.membership_id = "M123"
    mock_activity.membership_type = "Premium"
    mock_activity.activity = "Gym"
    mock_activity.revenue = 50.0
    mock_activity.duration = 60
    mock_activity.location = "Main Branch"

    # Mock quarterly performance data
    mock_performance = Mock()
    mock_performance.id = 1
    mock_performance.year = 2024
    mock_performance.quarter = "Q1"
    mock_performance.revenue = 250000
    mock_performance.memberships_sold = 100
    mock_performance.duration = 90

    # Create and configure mock repositories
    company_repo = Mock()
    company_repo.get_all.return_value = [mock_company]
    company_repo.get_by_id.return_value = mock_company

    activity_repo = Mock()
    activity_repo.get_all.return_value = [mock_activity]

    performance_repo = Mock()
    performance_repo.get_all.return_value = [mock_performance]

    return company_repo, activity_repo, performance_repo

@pytest.fixture
def app(mock_repositories):
    app = Flask(__name__)
    company_repo, activity_repo, performance_repo = mock_repositories
    
    controller = OverallController(
        company_repo,
        activity_repo,
        performance_repo
    )

    test_blueprint = Blueprint('overall_test', __name__)
    controller.register_routes(test_blueprint)
    
    app.register_blueprint(test_blueprint, url_prefix='/api/data')
    
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_all_data(client):
    response = client.get('/api/data/')
    print(response.json)
    assert response.status_code == 200
    data = response.json
    
    assert isinstance(data, list)
    assert len(data) == 3
    
    json_data = data[0][0]
    assert 'id' in json_data
    assert 'name' in json_data
    assert 'employees' in json_data
    assert 'performance' in json_data

    csv_data = data[1][0]
    assert 'membership_id' in csv_data
    assert 'activity' in csv_data
    assert 'revenue' in csv_data

    pdf_data = data[2][0]
    assert 'year' in pdf_data
    assert 'quarter' in pdf_data
    assert 'revenue' in pdf_data

def test_get_json_data(client):
    response = client.get('/api/data/json')
    assert response.status_code == 200
    data = response.json
    
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'employees' in data[0]
    assert 'performance' in data[0]

def test_get_csv_data(client):
    response = client.get('/api/data/csv')
    assert response.status_code == 200
    data = response.json
    
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'membership_id' in data[0]
    assert 'activity' in data[0]

def test_get_pdf_data(client):
    response = client.get('/api/data/pdf')
    assert response.status_code == 200
    data = response.json
    
    assert isinstance(data, list)
    assert len(data) > 0
    assert 'year' in data[0]
    assert 'quarter' in data[0]

def test_get_unsupported_data_type(client):
    response = client.get('/api/data/xml')
    assert response.status_code == 400
    assert response.json['error'] == 'Unsupported file type' 