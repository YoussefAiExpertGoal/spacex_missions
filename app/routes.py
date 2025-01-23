from flask import Blueprint, render_template, abort, request, jsonify
from app.models.spacex_models import DataManager
from app import cache
import logging

main = Blueprint('main', __name__)
data_manager = DataManager()

@main.route('/')
@cache.cached(timeout=300)
def index():
    missions_totales = data_manager.fetch_all_missions()
        
    missions_totales.sort(key=lambda x: x.date, reverse=True)
        
    nombre_total_missions = len(missions_totales)
    missions_reussies = sum(1 for mission in missions_totales if mission.success == True)
    missions_echouees = nombre_total_missions - missions_reussies
        
    statistiques = {
        'total': nombre_total_missions,
        'successful': missions_reussies,
        'failed': missions_echouees
        }
        
    return render_template('missions.html', 
                             missions=missions_totales,
                             stats=statistiques)