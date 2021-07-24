import boto3
import os
from glob import glob
import psycopg2
from dotenv import load_dotenv

load_dotenv()
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
PORT = os.getenv('PORT')
"""
This script download the files from s3-bucket, decompress and read them, connected to redshift db.
"""


def download_all_files():
    #initiate s3 resource
    s3 = boto3.resource('s3')

    # select bucket
    my_bucket = s3.Bucket('yzo-bucket')

    # download file into current directory
    for s3_object in my_bucket.objects.all():
        filename = s3_object.key
        my_bucket.download_file(s3_object.key, filename)

def decompress_files(path):
    list_of_files = glob(f"{path}*.gz") # list gzip files
    for file in list_of_files:
        bash_command = 'gzip -dk ' + '"' + file + '"'  
        os.system(bash_command) # Run command in Terminal 


def load_into_redshift_db():
    con = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=PORT)
    cur = con.cursor()

    cur.execute("begin;")

    cur.execute("select * from users ;")
    print(cur.fetchall())

    cur.close() 
    con.close()

    print("Copy executed fine!")



if __name__ == "__main__":
    #download_all_files()
    #decompress_files("/mnt/c/Users/owner/Desktop/Task2/")
    load_into_redshift_db()