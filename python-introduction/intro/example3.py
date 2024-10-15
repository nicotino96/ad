def dental_insurance_cost(company_name):
    if company_name == "Ratoncito Pérez S.L.":
        return "40"
    else:
        return 30

if __name__ == '__main__':
    company = "Dientes Sanos S.L."
    cost = dental_insurance_cost(company)
    print("Tu seguro dental con la compañía " + company + " cuesta " + str(cost) + " euros al mes")
