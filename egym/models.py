import json

class EgymModel(object):
    """ Base class from which all egym models will inherit. """

    def __init__(self, **kwargs):
        self.param_defaults = {}

    def __str__(self):
        """ Returns a string representation of EgymModel. By default
        this is the same as AsJsonString(). """
        return self.AsJsonString()

    def AsJsonString(self):
        """ Returns the EgymModel as a JSON string based on key/value
        pairs returned from the AsDict() method. """
        return json.dumps(self.AsDict(), sort_keys=True)

    def AsDict(self):
        """ Create a dictionary representation of the object. Please see inline
        comments on construction when dictionaries contain EgymModels. """
        data = {}

        for (key, value) in self.param_defaults.items():

            if isinstance(getattr(self, key, None), (list, tuple, set)):
                data[key] = list()
                for subobj in getattr(self, key, None):
                    if getattr(subobj, 'AsDict', None):
                        data[key].append(subobj.AsDict())
                    else:
                        data[key].append(subobj)

            elif getattr(getattr(self, key, None), 'AsDict', None):
                data[key] = getattr(self, key).AsDict()

            elif getattr(self, key, None):
                data[key] = getattr(self, key, None)
        return data

    @classmethod
    def NewFromJsonDict(cls, data, **kwargs):
        """ Create a new instance based on a JSON dict. Any kwargs should be
        supplied by the inherited, calling class.
        Args:
            data: A JSON dict, as converted from the JSON in the egym API.
        """

        json_data = data.copy()
        if kwargs:
            for key, val in kwargs.items():
                json_data[key] = val

        c = cls(**json_data)
        c._json = data
        return c

class Session(EgymModel):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'template': None,
            'sessionDate':None,
            'sessionIsoDate': None, 
            'exercises': None,
            'points': None,
        }
        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

        """if 'exercises' in kwargs:
            ex = []
            for e in kwargs.get('exercises'):
                ex.append(Exercise.NewFromJsonDict(e))
            self.exercises = ex"""

    def getTemplate(self):
        return self.getTemplate

    def getSessionDate(self):
        return self.sessionDate
    
    def getIsoDate(self):
        return self.sessionIsoDate

    def getExercises(self):
        return self.exercises

    def getPoints(self):
        return int(self.points)

class Exercise(EgymModel):

    def __init__(self, **kwargs):
        self.param_defaults = {
            'exercisetype': None,
            'uniqueExerciseClientId': None,
            'exerciseId': None,
            'generalExerciseIdcises': None,
            'sets': None, 
            'done': None,
            'dataSource': None,
            'points': None,
            'created': None,
        }
        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))
        
        if 'sets' in kwargs:
            sets = []
            for e in kwargs.get('sets'):
                sets.append(Set.NewFromJsonDict(e))
            self.sets = sets

    def getExerciseType(self):
        return self.exerciseType

    def getUniqueExerciseClientId(self):
        return self.uniqueExerciseClientId

    def getExerciseId(self):
        return self.exerciseId

    def getGeneralExerciseId(self):
        return self.generalExerciseId

    def getDone(self):
        return self.done

    def getDataSource(self):
        return self.dataSource

    def getPoints(self):
        return self.points

    def getCreated(self):
        return self.created

    def getSets(self):
        return self.sets

class Set(EgymModel):
               
    def __init__(self, **kwargs):
        self.param_defaults = {
            "setType": None,
            "numberOfReps": None,
            "weight": None,
        }
        for (param, default) in self.param_defaults.items():
            setattr(self, param, kwargs.get(param, default))

    def getSetType(self):
        return int(self.setType)

    def getWeight(self):
        return int(self.weight)

    def getReps(self):
        return int(self.numberOfReps)
