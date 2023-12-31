import pandas as pd

from source.entity.config_entity import TrainingPipelineConfig


if __name__ == '__main__':
    print_hi('PyCharm')

    train_pipeline_config_obj = TrainingPipelineConfig()

    print(train_pipeline_config_obj.__dict__)