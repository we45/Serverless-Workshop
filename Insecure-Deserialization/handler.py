import yaml
import json
from base64 import b64encode


def main(event, context):
    if 'body' in event:
        yfile = json.loads(event['body'])
        ycontent = yaml.load(yfile['file'])
        if 'reason' in ycontent:
            ycontent['reason'] = b64encode(ycontent['reason']).decode()
        return {"statusCode": 200, "body": json.dumps({"content": ycontent})}