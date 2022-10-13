import logging
import json

import ezocalc.mapper


def handler(event, context):

    print("PAYLOAD", event)

    calculator = ezocalc.mapper.Mapper()

    formula = json.loads(event['body'])['formula']

    calctree = calculator.scan(formula)
    result = calctree.get_value()

    print("RESULT", str(result))

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "formula": formula,
            "result": str(result)
        })
    }
