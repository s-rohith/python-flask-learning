from app import app

# Error Handling
@app.errorhandler(404)
def not_found_exception(error):
    return ({'Error': 404, 'Message': 'Requested URL not found'}), 404