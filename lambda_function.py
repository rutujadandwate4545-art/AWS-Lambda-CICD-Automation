
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    logger.info("AWS Lambda CI/CD Automation Started")
    logger.info("Received event: %s", json.dumps(event))

    detail = event.get("detail", {})
    pipeline_name = detail.get("pipeline", "Unknown")
    state = detail.get("state", "Unknown")
    execution_id = detail.get("execution-id", "Unknown")

    logger.info("Pipeline Name: %s", pipeline_name)
    logger.info("Pipeline State: %s", state)
    logger.info("Execution ID: %s", execution_id)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "CI/CD automation event processed successfully",
            "pipeline": pipeline_name,
            "state": state
        })
    }
