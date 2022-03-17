import sys
from os.path import basename

from pytest_ibutsu.artifact import Artifact
from pytest_ibutsu.aws import AWSClient


def upload_artifact(artifact_path):
    aws = AWSClient()
    artifact = Artifact()
    artifact.name = basename(artifact_path)
    artifact.path = artifact_path

    try:
        # upload file to S3 bucket
        aws.upload_file(file_path=artifact.path, file_name=artifact.name)
        # send message to SQS
        response = aws.send_message(artifact=artifact)
        response["ResponseMetadata"]["HTTPStatusCode"] == 200
    except KeyboardInterrupt:
        print("[CTRL+C detected]")
        aws.abort_transaction(artifact_name=artifact.name)
        sys.exit(1)
    except Exception:
        aws.abort_transaction(artifact_name=artifact.name)
        print("*** check your AWS credentials ***")
        sys.exit(1)
