from aws_cdk import (
    aws_iam as iam,
    aws_lambda as lambda_,
    aws_s3 as s3,
    App,
    Stack,
    Duration
)
from constructs import Construct
from os import path


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        fn = lambda_.Function(    
        scope=self, 
        id="hello-world-func",
        runtime=lambda_.Runtime.PYTHON_3_12,
        code=lambda_.Code.from_asset("lambda_functions/code"),
        handler="lambda_handler.handler",
        timeout=Duration.seconds(amount=30),
        
        )
    