def optimize(tasks):
    
    durations = {
        "Survey land":2,
        "Obtain permits":5,
        "Clear site":3,
        "Level ground":3,
        "Arrange materials":2,
        "Excavation":4,
        "Pour foundation":5,
        "Build columns":6,
        "Roof slab":7,
        "Inspection":2
    }
    
    schedule = []
    
    for t in tasks:
        schedule.append(f"{t} ({durations.get(t,3)} days)")
    
    return schedule
