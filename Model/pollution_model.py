from typing import Optional, List
from pydantic import BaseModel
from datetime import date

class PollutionModel(BaseModel):
    id: Optional[int]
    country: Optional[str]
    state: Optional[str]
    city: Optional[str]
    station: Optional[str]
    last_update:Optional[str]
    pollutant_id: Optional[str]
    pollutant_min:Optional[str]
    pollutant_max: Optional[str]
    pollutant_avg: Optional[str]
    pollutant_unit: Optional[str]

    class config:
        allow_population_by_field_name = True
        fields= {'id':{'alias':'id'},
                 'country':{'alias':'country'},
                 'state':{'alias':'state'},
                 'city':{'alias':'city'},
                 'station':{'alias':'station'},
                 'last_uppdate':{'alias':'last_update'},
                 'pollutant_id':{'alias':'pollution_id'},
                 'pollutant_min': {'alias': 'pollution_min'},
                 'pollutant_max': {'alias': 'pollution_max'},
                 'pollutant_avg': {'alias': 'pollution_avg'},
                 'pollutant_unit': {'alias': 'pollution_unit'}
        }

