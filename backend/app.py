from flask import Flask
from .models import db
from .config import config
from .repositories.company_repository import CompanyRepository
from .services.data_loader_service import DataLoaderService
from .services.csv_loader_service import CSVLoaderService
from .services.pptx_loader_service import PPTXLoaderService
from .routes.company_routes import company_blueprint, CompanyController
from .repositories.member_activity_repository import MemberActivityRepository
from .routes.member_activity_routes import member_activity_blueprint, MemberActivityController
from .repositories.quarterly_performance_repository import QuarterlyPerformanceRepository
from .routes.quarterly_performance_routes import quarterly_performance_blueprint, QuarterlyPerformanceController
from .services.pdf_loader_service import PDFLoaderService
from .routes.overall_routes import overall_blueprint, OverallController
from .repositories.revenue_distribution_repository import RevenueDistributionRepository
from .routes.revenue_distribution_routes import revenue_distribution_blueprint, RevenueDistributionController
from .repositories.key_highlights_repository import KeyHighlightsRepository
from .routes.key_highlights_routes import key_highlights_blueprint, KeyHighlightsController
import json
from flask_cors import CORS

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    CORS(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        
        company_repository = CompanyRepository(db)
        member_activity_repository = MemberActivityRepository(db)
        quarterly_performance_repository = QuarterlyPerformanceRepository(db)
        revenue_distribution_repository = RevenueDistributionRepository(db)
        key_highlights_repository = KeyHighlightsRepository(db)
        
        data_loader_service = DataLoaderService(company_repository, db)
        csv_loader_service = CSVLoaderService(db)
        pdf_loader_service = PDFLoaderService(quarterly_performance_repository, db)
        pptx_loader_service = PPTXLoaderService(db)
        
        company_controller = CompanyController(company_repository)
        company_controller.register_routes(company_blueprint)
        
        member_activity_controller = MemberActivityController(member_activity_repository)
        member_activity_controller.register_routes(member_activity_blueprint)
        
        quarterly_performance_controller = QuarterlyPerformanceController(quarterly_performance_repository)
        quarterly_performance_controller.register_routes(quarterly_performance_blueprint)
        
        revenue_distribution_controller = RevenueDistributionController(revenue_distribution_repository)
        revenue_distribution_controller.register_routes(revenue_distribution_blueprint)
        
        key_highlights_controller = KeyHighlightsController(key_highlights_repository)
        key_highlights_controller.register_routes(key_highlights_blueprint)

        overall_controller = OverallController(company_repository, member_activity_repository, quarterly_performance_repository, key_highlights_repository, revenue_distribution_repository)
        overall_controller.register_routes(overall_blueprint)

        app.register_blueprint(company_blueprint, url_prefix='/api/companies')
        app.register_blueprint(member_activity_blueprint, url_prefix='/api/activities')
        app.register_blueprint(quarterly_performance_blueprint, url_prefix='/api/quarterly-performance')
        app.register_blueprint(revenue_distribution_blueprint, url_prefix='/api/revenue-distribution')
        app.register_blueprint(key_highlights_blueprint, url_prefix='/api/key-highlights')
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
            app.logger.warning('pptx dataset not found')
        except Exception as e:
            app.logger.error(f'Error loading PPTX data: {str(e)}')


    return app

if __name__ == '__main__':
    app = create_app()
    app.run()