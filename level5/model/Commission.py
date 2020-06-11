from .Options import Options


class Commission:
    """Class Commission"""
    COMMISSION_MULT = 0.3
    INSURANCE_MULT = 0.5
    ASSISTANCE_MULT = 100

    @classmethod
    def compute_commission(cls, n_days, price, options=None):
        """Compute commission
        Usage of Class 'Options' to compute additionnal feature

        :param n_days: Took from Rental Class Object
        :param price: Took from Rental Class Object
        :param otpions: Contains optionals feature desired by the Driver, example -> ['gps', 'baby_seat']
        """
        commission_fee = int(price * Commission.COMMISSION_MULT)

        driver_price = price
        owner_fee = driver_price - commission_fee

        insurance_fee = int(commission_fee / 2)
        assurance_fee = n_days * 100    # 1€ = 100 cents
        drivy_fee = commission_fee - insurance_fee - assurance_fee

        if options:
            gps_fee, baby_seat_fee, additional_insurance = Options.get_additionnal_fee(
                n_days, options)

            owner_fee += gps_fee + baby_seat_fee
            driver_price += gps_fee + baby_seat_fee + additional_insurance
            drivy_fee += additional_insurance

        commission = {
            "driver": driver_price,
            "owner": owner_fee,
            "insurance": insurance_fee,
            "assistance": assurance_fee,
            "drivy": drivy_fee
        }

        return commission
