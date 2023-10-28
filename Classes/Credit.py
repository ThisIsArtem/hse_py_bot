class Credit:
    def __init__(self, summ, period, perc):
        self.summ = summ
        self.period = period
        self.perc = perc

    def dif_int(self):
        r = self.perc / 100 / 12
        m = self.period * 12
        d = self.summ / m

        total_payment = 0
        for i in range(1, int(m + 1)):
            interest_payment = (self.summ - (i - 1) * d) * r
            total_payment += d + interest_payment

        return round(d, 2), round(total_payment, 2)

    def ann_int(self):
        perc_in_month = self.perc / (12 * 100)
        months_pay = self.summ * (perc_in_month * (1 + perc_in_month)
                                  ** (self.period * 12)) / ((1 + perc_in_month) ** (self.period * 12) - 1)
        total_pay = months_pay * 12 * self.period
        return round(months_pay, 2), round(total_pay, 2)

    def deposit_total_amount(self):
        perc = self.perc / 100
        return round(self.summ * (1 + perc / 12) ** self.period, 2)

