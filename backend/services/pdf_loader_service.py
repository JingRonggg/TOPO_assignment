import PyPDF2
from ..models import QuarterlyPerformance

class PDFLoaderService:
    def __init__(self, quarterly_performance_repository, db):
        self.repository = quarterly_performance_repository
        self.db = db

    def load_pdf_data(self, file_path):
        try:
            data = self._extract_data_from_pdf(file_path)
            self._clear_existing_data()
            for record in data:
                performance = QuarterlyPerformance(
                    year=record['year'],
                    quarter=record['quarter'],
                    revenue=record['revenue'],
                    memberships_sold=record['memberships_sold'],
                    duration=record['duration']
                )
                self.repository.create(performance)
            
            return True
        except Exception as e:
            self.db.session.rollback()
            raise e

    def _extract_data_from_pdf(self, file_path):
        data = []
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = pdf_reader.pages[0].extract_text()
                rows = text.split('\n')
                rows = rows[2:]
                for row in rows:
                    parts = row.strip().split()
                    if len(parts) >= 4:
                        data.append({
                            'year': int(parts[0]),
                            'quarter': str(parts[1]),
                            'revenue': float(parts[2].replace('$', '').replace(',', '')),
                            'memberships_sold': int(parts[3]),
                            'duration': int(parts[4])
                        })
            return data
        except Exception as e:
            raise ValueError(f"Error extracting data from PDF: {str(e)}")

    def _clear_existing_data(self):
        try:
            QuarterlyPerformance.query.delete()
            self.db.session.commit()
        except Exception:
            self.db.session.rollback()
            raise 