from flask import Flask
from models import db
from config import config
from repositories.company_repository import CompanyRepository
from services.data_loader_service import DataLoaderService
from services.csv_loader_service import CSVLoaderService
from routes.company_routes import company_blueprint, CompanyController
from repositories.member_activity_repository import MemberActivityRepository
from routes.member_activity_routes import member_activity_blueprint, MemberActivityController
from repositories.quarterly_performance_repository import QuarterlyPerformanceRepository
from routes.quarterly_performance_routes import quarterly_performance_blueprint, QuarterlyPerformanceController
from services.pdf_loader_service import PDFLoaderService
from routes.overall_routes import overall_blueprint, OverallController
from repositories.annual_summary_repository import AnnualSummaryRepository
from repositories.quarterly_metrics_repository import QuarterlyMetricsRepository
from repositories.revenue_by_activity_repository import RevenueByActivityRepository
from services.pptx_loader_service import PPTXLoaderService
from routes.pptx_data_routes import pptx_data_blueprint, PPTXDataController
import json

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
        company_repository = CompanyRepository(db)
        member_activity_repository = MemberActivityRepository(db)
        quarterly_performance_repository = QuarterlyPerformanceRepository(db)
        annual_summary_repo = AnnualSummaryRepository(db)
        quarterly_metrics_repo = QuarterlyMetricsRepository(db)
        revenue_by_activity_repo = RevenueByActivityRepository(db)
        
        data_loader_service = DataLoaderService(company_repository, db)
        csv_loader_service = CSVLoaderService(db)
        pdf_loader_service = PDFLoaderService(quarterly_performance_repository, db)
        pptx_loader_service = PPTXLoaderService(
            annual_summary_repo,
            quarterly_metrics_repo,
            revenue_by_activity_repo,
            db
        )

        company_controller = CompanyController(company_repository)
        company_controller.register_routes(company_blueprint)
        member_activity_controller = MemberActivityController(member_activity_repository)
        member_activity_controller.register_routes(member_activity_blueprint)
        
        quarterly_performance_controller = QuarterlyPerformanceController(quarterly_performance_repository)
        quarterly_performance_controller.register_routes(quarterly_performance_blueprint)
        
        overall_controller = OverallController(company_repository, member_activity_repository, quarterly_performance_repository)
        overall_controller.register_routes(overall_blueprint)

        pptx_controller = PPTXDataController(
            annual_summary_repo,
            quarterly_metrics_repo,
            revenue_by_activity_repo
        )
        pptx_controller.register_routes(pptx_data_blueprint)

        app.register_blueprint(company_blueprint, url_prefix='/api/companies')
        app.register_blueprint(member_activity_blueprint, url_prefix='/api/activities')
        app.register_blueprint(quarterly_performance_blueprint, url_prefix='/api/quarterly-performance')
        app.register_blueprint(pptx_data_blueprint, url_prefix='/api/pptx-data')
        app.register_blueprint(overall_blueprint, url_prefix='/api/data')
        
        try:
            with open('datasets/dataset1.json', 'r') as file:
                data = json.load(file)
                data_loader_service.load_json_data(data)
        except FileNotFoundError:
            app.logger.warning('JSON dataset not found')
        except Exception as e:
            app.logger.error(f'Error loading JSON data: {str(e)}')

        try:
            csv_loader_service.load_csv_data('datasets/dataset2.csv')
        except FileNotFoundError:
            app.logger.warning('CSV dataset not found')
        except Exception as e:
            app.logger.error(f'Error loading CSV data: {str(e)}')

        try:
            pdf_loader_service.load_pdf_data('datasets/dataset3.pdf')
        except FileNotFoundError:
            app.logger.warning('PDF dataset not found')
        except Exception as e:
            app.logger.error(f'Error loading PDF data: {str(e)}')

        try:
            pptx_loader_service.load_pptx_data('datasets/dataset4.pptx')
        except FileNotFoundError:
            app.logger.warning('PowerPoint dataset not found')
        except Exception as e:
            app.logger.error(f'Errpr loading PowerPoint data: {str(e)}')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run()