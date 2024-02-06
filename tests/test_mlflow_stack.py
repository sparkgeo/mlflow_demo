import aws_cdk as core
import aws_cdk.assertions as assertions

from mlflow_simple_aws.mlflow_stack import MlFlowStack


# example tests. To run these tests, uncomment this file along with the example
# resource in tmp/tmp_stack.py
def test_s3_created():
    app = core.App()
    stack = MlFlowStack(app, "mlflow-stack")
    template = assertions.Template.from_stack(stack)


#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
