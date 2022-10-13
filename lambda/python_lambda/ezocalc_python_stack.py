from aws_cdk import (
    Stack,
)
from constructs import Construct

from python_lambda.EzoCalcFunctionStack import EzoCalcFunctionStack

class EzocalcPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # --- Calculator ---
        self.linkedin_payload_lambda = EzoCalcFunctionStack(self)
