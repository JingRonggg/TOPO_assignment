from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Company(db.Model):
    __tablename__ = 'companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(100))
    revenue = db.Column(db.Float)
    location = db.Column(db.String(100))
    employees = db.relationship('Employee', backref='company', lazy=True)
    performance = db.relationship('CompanyPerformance', backref='company', lazy=True)

class Employee(db.Model):
    __tablename__ = 'employees'
    
    id = db.Column(db.String(10), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100))
    salary = db.Column(db.Float)
    hired_date = db.Column(db.Date)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)

class CompanyPerformance(db.Model):
    __tablename__ = 'company_performance'
    
    id = db.Column(db.Integer, primary_key=True)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    quarter = db.Column(db.String(10), nullable=False)
    revenue = db.Column(db.Float)
    profit_margin = db.Column(db.Float)

class MemberActivity(db.Model):
    __tablename__ = 'member_activities'
    
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    membership_id = db.Column(db.String(10), nullable=False)
    membership_type = db.Column(db.String(50), nullable=False)
    activity = db.Column(db.String(100), nullable=False)
    revenue = db.Column(db.Float)
    duration = db.Column(db.Integer)
    location = db.Column(db.String(100))

class QuarterlyPerformance(db.Model):
    __tablename__ = 'quarterly_performance'
    
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    quarter = db.Column(db.String, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    memberships_sold = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('year', 'quarter', name='unique_year_quarter'),
    )

class AnnualSummary(db.Model):
    __tablename__ = 'annual_summary'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    total_revenue = db.Column(db.Integer, nullable=False)
    total_membership_sold = db.Column(db.Integer, nullable=False)
    top_location = db.Column(db.String, nullable=False)

class QuaterlyMetrics(db.Model):
    __tablename__ = 'quaterly_metrics'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    quarter = db.Column(db.String, nullable=False)
    revenue = db.Column(db.Float, nullable=False)
    memberships_sold = db.Column(db.Integer, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('year', 'quarter', name='unique_year_quarter'),
    )

class RevenueByActivity(db.Model):
    __tablename__ = 'revenue_by_activity'

    id = db.Column(db.Integer, primary_key=True)
    gym = db.Column(db.Float)
    pool = db.Column(db.Float)
    tennis_court = db.Column(db.Float)
    personal_training = db.Column(db.Float)
    others = db.Column(db.Float)