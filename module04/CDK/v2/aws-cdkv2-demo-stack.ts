import { RemovalPolicy, Stack, StackProps } from "aws-cdk-lib";
import { Construct } from "constructs";
import * as lambda from "aws-cdk-lib/aws-lambda";
import * as apigateway from "aws-cdk-lib/aws-apigateway";
import * as path from "path";

export class AwsCdkv2DemoStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const myFunction = new lambda.Function(this, "myLambdaFunctionByCDKv2", {
      functionName: "aws-cdk-demo-function",
      code: lambda.Code.fromAsset(path.join(__dirname, "../src")),
      runtime: lambda.Runtime.PYTHON_3_8,
      handler: "index.lambda_handler",
    });

    const api = new apigateway.RestApi(this, "api", {
      restApiName: "aws-cdk-demo-api",
    });
    const integration = new apigateway.LambdaIntegration(myFunction);
    api.root.addResource("hello").addMethod("GET", integration);
    //
  }
}