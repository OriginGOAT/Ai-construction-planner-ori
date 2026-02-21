def validate(tasks, resources):
    
    issues = []
    
    if (resources or {}).get("workers",0) < 5:
        issues.append("Insufficient workforce")
        
    if (resources or {}).get("cement",0) < 300:
        issues.append("Cement shortage")
        
    if (resources or {}).get("excavators",0) < 1:
        issues.append("Excavator unavailable")
        
    if (resources or {}).get("budget",0) < 500000:
        issues.append("Budget risk")
    
    return issues
