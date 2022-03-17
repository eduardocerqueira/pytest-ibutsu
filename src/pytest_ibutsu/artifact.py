import datetime
import uuid

from pytest_ibutsu.util import tarfile_mock


class Artifact:
    def __init__(self):
        self.name = None
        self.path = None

    @staticmethod
    def artifact_mock(total):
        artifact_list = []
        for i in range(total):
            artifact = Artifact()
            artifact.name = f"artifact-{str(uuid.uuid4())[:4]}.tar.gz"
            artifact.path = tarfile_mock(artifact.name)
            artifact_list.append(artifact)
        return artifact_list

    @staticmethod
    def set_name():
        now = datetime.datetime.now()
        name = f"artifact-{now.minute}{now.second}-{str(uuid.uuid4())[:4]}.tar.gz"
        return name
