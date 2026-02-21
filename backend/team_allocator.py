def allocate(workers):

    if workers<5:
        return "Single team allocation"

    if workers<10:
        return "Dual team allocation"

    return "Multi crew deployment"
