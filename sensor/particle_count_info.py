from house_info import HouseInfo
from datetime import date, datetime

class ParticleData(HouseInfo):
    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("particulate", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("particulate", rec_date)
        return self._convert_data(recs)

    def get_data_concentrations(self, data):
        particulate = {"good" : 0, "moderate" : 0, "bad" : 0}
        for rec in data:
            if float(rec) <= 50:
                particulate.setdefault("good", int(rec))
            elif 50 <= float(rec) <= 100:
                particulate.setdefault("moderate", int(rec))
            elif float(rec) > 100:
                particulate.setdefault("bad", int(rec))
        return particulate




        