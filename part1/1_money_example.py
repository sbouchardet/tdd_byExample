#!../env/bin/python

exchange =[
{'from':'CHF', 'to':'USD', 'rate':1.0/1.5},
{'from':'USD', 'to':'CHF', 'rate':1.5},
{'from':'BRS', 'to':'USD', 'rate':3.5}
]

class Dolar:
    def __init__(self,amount):
        self.__amount=amount
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__amount == other.__amount
        else:
            return False

    def times(self,multiplier):
        return Dolar(self.__amount * multiplier)
    


class infos:

    total = -1
    def __init__(self, instrument,shares, price, currency):
            self.instrument = instrument
            self.shares = shares
            self.price = price
            self.currency = currency

    def __str__(self):
        return "%s - %d - %d - %s " % (self.instrument,self.shares,self.price,self.currency)

    def set_total(self):
        self.total=self.shares * self.price


class list_infos:

    def __init__(self, *all_infos):
        self.array_infos = all_infos

    def __str__(self):
        r = '';
        for i in self.array_infos:
            r = '%s \n %s \n' % (r,i);
        return r;

    def get_total(self,currency):
        tot=0.0
        rates = filter(lambda x: x['to']==currency,exchange)
        for inf in self.array_infos:
            inf.set_total()
            if inf.currency == currency:
                tot = tot + inf.total
            else:
                rate = filter(lambda x: x['from']==inf.currency,rates)[0]['rate']
                tot = tot + (inf.total * rate)

        return tot;
