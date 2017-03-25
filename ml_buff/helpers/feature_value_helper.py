from ml_buff.models.base_feature_record import BaseFeatureRecord
from ml_buff.models.base_input_data_repository import BaseInputDataRepository
from ml_buff.database import session_scope

class FeatureValueHelper():
    @classmethod
    def createAll(self, input_data_id_list):
        for input_data_id in input_data_id_list:
            self.createAllForInput(input_data_id)

    @classmethod
    def createAllForInput(self, input_data_id):
        subclasses = BaseFeatureRecord.__subclasses__()

        for subclass in subclasses:
            with session_scope() as session:
                input_instance = BaseInputDataRepository().get(session, input_data_id)
            feature = subclass()
            feature.getOrCreateValue(input_instance)           
            with session_scope() as session:
                input_instance = BaseInputDataRepository().get(session, input_data_id)


    @classmethod
    def forceUpdateForInput(self, input_data_id):
        subclasses = BaseFeatureRecord.__subclasses__()
        with session_scope() as session:
            input_data = BaseInputDataRepository(session, input_data_id)
            for subclass in subclasses:
                feature = subclass()
                feature.createValue(input_data)