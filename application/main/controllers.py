from flask import Blueprint

main = blueprint('main',__name__)

@main.route('/')
def index():
    return 'Main'
