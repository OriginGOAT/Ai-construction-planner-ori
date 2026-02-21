def risk(location):
    
    if not location:
        return "Weather data unavailable"
        
    if "himalaya" in location.lower():
        return "Heavy rainfall risk"
        
    return "Moderate weather risk"
