from docx import Document
import boto3
import urllib
from io import StringIO

s3 = boto3.resource('s3')

def main(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'])
    fileobj = s3.Object(bucket, key)
    with open("/tmp/Some.docx", "wb") as write_doc:
        write_doc.write(fileobj.get()['Body'].read())
    doc = Document("/tmp/Some.docx")
    for para in doc.paragraphs:
        print(para.text)