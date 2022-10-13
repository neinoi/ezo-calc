from aws_cdk import (
    aws_lambda,
    CfnOutput
)


class EzoCalcFunctionStack:

    def __init__(self, stack) -> None:

        # LinkedIn Payload frontend

        # Create role
        # linkedin_payloads_role = aws_iam.Role(scope=stack, id='linkedin-payloads-role',
        #                                       assumed_by=aws_iam.ServicePrincipal('lambda.amazonaws.com'),
        #                                       role_name='linkedin-payloads-role',
        #                                       managed_policies=[
        #                                           aws_iam.ManagedPolicy.from_aws_managed_policy_name(
        #                                               'service-role/AWSLambdaVPCAccessExecutionRole'),
        #                                           aws_iam.ManagedPolicy.from_aws_managed_policy_name(
        #                                               'service-role/AWSLambdaBasicExecutionRole')
        #                                       ])

        # Defines an AWS Lambda resource
        linkedin_payloads_lambda = aws_lambda.Function(
            stack, 'ezocalc-lambda',
            runtime=aws_lambda.Runtime.PYTHON_3_7,
            function_name='ezocalc-lambda',
            description='Ezo calc sample lambda function',
            code=aws_lambda.Code.from_asset("./lambdas"),
            handler='EzoCalcFunction.handler',
            # role=linkedin_payloads_role,
            environment={
                'NAME': 'ezocalc-lambda'
            }
        )

        fnUrl = linkedin_payloads_lambda.add_function_url(auth_type=aws_lambda.FunctionUrlAuthType.NONE)
        CfnOutput(stack, "LambdaUrl", value=fnUrl.url)