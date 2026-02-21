def mitigate(issues):

    actions=[]

    for i in issues:

        if "workforce" in i:
            actions.append("Hire temporary labor")

        if "Cement" in i:
            actions.append("Contact secondary vendor")

        if "Excavator" in i:
            actions.append("Lease equipment")

        if "Budget" in i:
            actions.append("Reduce project scope")

    return actions
