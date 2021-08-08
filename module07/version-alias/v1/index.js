let response;
var fs = require('fs');
var filename;

exports.handler = async (event, context) => {
    try {
        var foo = 'hello';
        filename = "./v1.html";

        var contents = fs.readFileSync(filename, 'utf8');

        response = {
            'statusCode': 200,
            'headers': {
                "Content-Type": "text/html; charset=utf-8"
            },
            'body': contents
        };
    } catch (err) {
        console.log(err);
        return err;
    }

    return response;
};
