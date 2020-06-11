class Commission:
    """Class Commission"""
    COMMISSION_MULT = 0.3
    INSURANCE_MULT = 0.5
    ASSISTANCE_MULT = 100

    @classmethod
    def compute_commission(cls, n_days, price):
        """Compute commission

        :param n_days: Took from Rental Class Object
        :param price: Took from Rental Class Object
        """
        commission_fee = int(price * Commission.COMMISSION_MULT)

        insurance_fee = int(commission_fee / 2)
        assurance_fee = n_days * 100    # 1€ = 100 cents
        drivy_fee = commission_fee - insurance_fee - assurance_fee

        commission = {
            "insurance_fee": insurance_fee,
            "assistance_fee": assurance_fee,
            "drivy_fee": drivy_fee
        }

        return commission
