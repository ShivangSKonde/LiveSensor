# from sensor.constant.training_pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME
import os
class TargetValueMapping:
    # mapping negative value as 0 and positive value as 1
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1

    def to_dict(self):
        return self.__dict__

    # Reverse mapping 0 value equal to negative and 1 equal to positive
    def reverse_mapping(self):
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(), mapping_response.keys()))