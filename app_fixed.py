#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LUXLAB OMNISYSTEM v10.0 - PRODUCTION VERSION
Sistema senza emoji per server Linux
"""

import os
import sys
import locale

# Fix encoding per Linux
if sys.platform == 'linux':
    os.environ['PYTHONIOENCODING'] = 'utf-8'

from flask import Flask, request, jsonify, render_template, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import logging

# Configurazione base
app = Flask(__name__)
app.config['SECRET_KEY'] = 'luxlab-2024-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///luxlab.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
CORS(app)

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    nome = db.Column(db.String(100))

# Routes
@app.route('/')
def index():
    """Usa template HTML separato invece di string"""
    return render_template('index.html')

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'operational',
        'version': 'v10.0-CLEAN'
    })

# Blocca scanner PHP
@app.route('/<path:path>')
def catch_all(path):
    """Blocca tutti i tentativi di scan"""
    if path.endswith('.php'):
        logger.warning(f"Blocked PHP scan attempt: {path}")
        return "Not Found", 404
    return "Not Found", 404

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    print("="*50)
    print("LUXLAB OMNISYSTEM v10.0 - CLEAN VERSION")
    print("Server running on: http://0.0.0.0:5000")
    print("="*50)
    
    app.run(host='0.0.0.0', port=8080, debug=False)
