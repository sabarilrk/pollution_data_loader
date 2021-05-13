from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

class PollutionModel(BaseModel):
    id: Optional[int]
    country: Optional[str]
    state: Optional[str]
    city: Optional[str]
    station: Optional[str]
    last_update:Optional[datetime]
    pollution_id: Optional[str]
    pollution_min:Optional[int]
    pollution_max: Optional[int]
    pollution_avg: Optional[int]
    pollution_unit: Optional[str]

    class config:
        allow_population_by_field_name = True
        fields= {'id':{'alias':'id'},
                'country':{'alias':'country'},
                'state':{'alias':'state'},
                'city':{'alias':'city'}
         }

