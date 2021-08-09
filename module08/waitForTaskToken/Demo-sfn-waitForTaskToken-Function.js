console.log('Loading function');
const aws = require('aws-sdk');

exports.handler = (event, context, callback) => {
    const stepfunctions = new aws.StepFunctions();

    console.log(event);

    for (const record of event.Records) {
        const messageBody = JSON.parse(record.body);
        const input_data = messageBody.Input;
        const taskToken_data = messageBody.TaskToken;
        console.log(taskToken_data)
        const output_data = "\"Hello," + input_data + "\"" ;
        const params = {
            output:    output_data,
            taskToken: taskToken_data
        };
        console.log(`Calling Step Functions to complete callback task with params ${JSON.stringify(params)}`);

        stepfunctions.sendTaskSuccess(params, (err, data) => {
            if (err) {
                console.error(err.message);
                callback(err.message);
                return;
            }
            console.log(data);
            callback(null);
        });
    }
};
