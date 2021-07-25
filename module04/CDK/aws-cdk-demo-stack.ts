import * as cdk from "@aws-cdk/core";
import { Asset } from "@aws-cdk/aws-s3-assets";
import * as lambda from "@aws-cdk/aws-lambda";
import * as apigateway from "@aws-cdk/aws-apigateway";
import * as path from "path";

export class AwsCdkDemoStack extends cdk.Stack {
  constructor(scope: cdk.Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // The code that defines your stack goes here
    const myFunction = new lambda.Function(this, "myLambdaFunctionByCDK", {
      functionName: "aws-cdk-demo-function",
      code: lambda.Code.fromAsset(path.join(__dirname, "../src")),
      runtime: lambda.Runtime.PYTHON_3_7,
      handler: "index.lambda_handler",
    });

    const api = new apigateway.RestApi(this, "api", {
      restApiName: "aws-cdk-demo-api",
    });
    const integration = new apigateway.LambdaIntegration(myFunction);
    api.root.addResource("hello").addMethod("GET", integration);
    
  }
}