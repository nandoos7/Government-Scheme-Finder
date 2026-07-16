def check_eligibility(user_data, schemes):

    eligible_schemes = []

    for _, scheme in schemes.iterrows():

        is_eligible = True

        # Age Check
        if user_data["age"] < scheme["MinAge"]:
            is_eligible = False

        if user_data["age"] > scheme["MaxAge"]:
            is_eligible = False

        # Income Check
        if user_data["income"] > scheme["IncomeLimit"]:
            is_eligible = False

        # Occupation Check
        if scheme["Occupation"] != "Any":
            if user_data["occupation"] != scheme["Occupation"]:
                is_eligible = False

        # Student Check
        if scheme["Student"] != "Any":
            if user_data["student"] != scheme["Student"]:
                is_eligible = False

        # Farmer Check
        if scheme["Farmer"] != "Any":
            if user_data["farmer"] != scheme["Farmer"]:
                is_eligible = False

        if is_eligible:
            eligible_schemes.append(scheme)

    return eligible_schemes