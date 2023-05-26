from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Medewerkers, Medewerkers_rol 

# Create engine
engine = create_engine('sqlite:///static/users.db')

# Create session
Session = sessionmaker(bind=engine)
session = Session()


# Initialize Flask app
app = Flask(__name__)



# Configure SQLAlchemy to use the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize SQLAlchemy with the app
db = SQLAlchemy(app)


# Move db.init_app(app) to this location
db.init_app(app)



@app.route('/')
def view_scrummasters():
    data = {
        "scrummasters": Medewerkers_rol.query.filter_by(rol_id='1').count(),
        "AC": Medewerkers_rol.query.filter_by(rol_id='2').count(),
        "AM": Medewerkers_rol.query.filter_by(rol_id='7').count(),
        "PJ": Medewerkers_rol.query.filter_by(rol_id='6').count(),
        "PO": Medewerkers_rol.query.filter_by(rol_id='3').count(),
        "RTE": Medewerkers_rol.query.filter_by(rol_id='4').count()
    }

    scrummasters = get_scrummasters()
    scrummasters_2024 = get_scrummasters_2024()
    agilecoaches_2024 = get_agilecoaches_2024()
    productowners_2024 = get_productowners_2024()
    RTE_2024 = get_RTE_2024()
    ATE_2024 = get_ATE_2024()
    projectmanager_2024 = get_projectmanagers_2024()
    PMO_2024 = get_PMO_2024()
    PGM_2024 = get_PGM_2024()
    productowners_2023 = get_productowners_2023()

    return render_template('index.html', productowners_2023=productowners_2023, data=data, scrummasters=scrummasters,
                           scrummasters_2024=scrummasters_2024, agilecoaches_2024=agilecoaches_2024,
                           productowners_2024=productowners_2024, RTE_2019=RTE_2024, ATE_2024=ATE_2024,
                           projectmanager_2024=projectmanager_2024, PMO_2024=PMO_2024, PGM_2024=PGM_2024)

# functie om het aantal scrummasters in 2022 op te halen
def get_scrummasters():
    query = """SELECT *
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2027-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'SM'))"""

    result = db.session.execute(query)
    return result.all()

# functie om het aantal scrummasters in 2024 op te halen 
def get_scrummasters_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'SM'))"""

    result = db.session.execute(query)
    return result.scalar()

# functie om het aantal agile coaches in 2019 te tellen
def get_agilecoaches_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                           FROM medewerkers_has_rol
                           WHERE rol_id = (SELECT id
                                           FROM rol
                                           WHERE rolnaam = 'AC'))"""

    result = db.session.execute(query)
    return result.scalar()

# functie om het aantal product owners in 2019 te tellen
def get_productowners_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                          FROM medewerkers_has_rol
                          WHERE rol_id = (SELECT id
                                          FROM rol
                                          WHERE rolnaam = 'PO'))"""

    result = db.session.execute(query)
    return result.scalar()

# functie om het aantal RTE in 2019 op te halen
def get_RTE_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                          FROM medewerkers_has_rol
                          WHERE rol_id = (SELECT id
                                          FROM rol
                                          WHERE rolnaam = 'RTE'))"""

    result = db.session.execute(query)
    return result.scalar()

# functie om het aantal ATE in 2019 op te halen
def get_ATE_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                          FROM medewerkers_has_rol
                          WHERE rol_id = (SELECT id
                                          FROM rol
                                          WHERE rolnaam = 'ATE'))"""

    result = db.session.execute(query)
    return result.scalar()

# functie om het aantal project managers in 2019 op te halen
def get_projectmanagers_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                          FROM medewerkers_has_rol
                          WHERE rol_id = (SELECT id
                                          FROM rol
                                          WHERE rolnaam = 'PJM'))"""

    result = db.session.execute(query)
    return result.scalar()

# functie om het aantal PMO in 2019 op te halen
def get_PMO_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                          FROM medewerkers_has_rol
                          WHERE rol_id = (SELECTid
                                          FROM rol
                                          WHERE rolnaam = 'PMO'))"""

    result = db.session.execute(query)
    return result.scalar()

# functie om het aantal PGM in 2019 op te halen
def get_PGM_2024():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2024-12-31'
               AND id IN (SELECT medewerker_id
                          FROM medewerkers_has_rol
                          WHERE rol_id = (SELECT id
                                          FROM rol
                                          WHERE rolnaam = 'PGM'))"""

    result = db.session.execute(query)
    return result.scalar()


def get_productowners_2023():
    query = """SELECT COUNT(*)
               FROM medewerkers
               WHERE einddatum_contract BETWEEN '1980-01-01' AND '2023-12-31'
               AND id IN (SELECT medewerker_id
                          FROM medewerkers_has_rol
                          WHERE rol_id = (SELECT id
                                          FROM rol
                                          WHERE rolnaam = 'PO'))"""

    result = db.session.execute(query)
    return result.scalar()

# route for the index page
@app.route('/users')
def view_users():
    data = {
        "scrummasters": Medewerkers_rol.query.filter_by(rol_id='1').count(),
        "AC": Medewerkers_rol.query.filter_by(rol_id='2').count(),
        "AM": Medewerkers_rol.query.filter_by(rol_id='7').count(),
        "PJ": Medewerkers_rol.query.filter_by(rol_id='6').count(),
        "PO": Medewerkers_rol.query.filter_by(rol_id='3').count(),
        "RTE": Medewerkers_rol.query.filter_by(rol_id='4').count()
    }
    return render_template('userlist.html', data=data)

if __name__ == '__main__':
    app.run()
