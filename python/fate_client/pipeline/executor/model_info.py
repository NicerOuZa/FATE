from typing import Union, Dict
from ..scheduler.runtime_constructor import RuntimeConstructor


class StandaloneModelInfo(object):
    def __init__(self, job_id: str, task_info: Dict[str, RuntimeConstructor]):
        self._job_id = job_id
        self._task_info = task_info

    @property
    def job_id(self):
        return self._job_id

    @property
    def task_info(self):
        return self._task_info


class FateFlowModelInfo(object):
    def __init__(self, job_id: str, model_id: str, model_version: str):
        self._job_id = job_id
        self._model_id = model_id
        self._model_version = model_version

    @property
    def job_id(self):
        return self._job_id

    @property
    def model_id(self):
        return self._model_id

    @property
    def model_version(self):
        return self._model_version