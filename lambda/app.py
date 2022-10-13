#!/usr/bin/env python3
import os

import aws_cdk as cdk
from aws_cdk import Tags

from python_lambda.ezocalc_python_stack import EzocalcPythonStack


app = cdk.App()
EzocalcPythonStack(app, "EzocalcPythonStack",
    # If you don't specify 'env', this stack will be environment-agnostic.
    # Account/Region-dependent features and context lookups will not work,
    # but a single synthesized template can be deployed anywhere.

    # Uncomment the next line to specialize this stack for the AWS Account
    # and Region that are implied by the current CLI configuration.

    #env=cdk.Environment(account=os.getenv('CDK_DEFAULT_ACCOUNT'), region=os.getenv('CDK_DEFAULT_REGION')),

    # Uncomment the next line if you know exactly what Account and Region you
    # want to deploy the stack to. */

    env=cdk.Environment(account='636921931117', region='ca-central-1'),

    # For more information, see https://docs.aws.amazon.com/cdk/latest/guide/environments.html
    )

Tags.of(app).add("PROJECT", "Ezocalc")
Tags.of(app).add("ENVIRONMENT", "dev")

app.synth()
