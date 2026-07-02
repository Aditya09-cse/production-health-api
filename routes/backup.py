import os
from datetime import datetime

import boto3
from flask import Blueprint, jsonify
from botocore.exceptions import ClientError

from config import Config

backup_bp = Blueprint("backup", __name__)


@backup_bp.route("/backup", methods=["POST"])
def backup_notes():
    try:
        s3 = boto3.client("s3", region_name=Config.AWS_REGION)

        file_name = "data/notes.json"

        if not os.path.exists(file_name):
            return jsonify({
                "error": "notes.json not found"
            }), 404

        backup_name = f"backup-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"

        s3.upload_file(
            file_name,
            Config.S3_BUCKET,
            backup_name
        )

        return jsonify({
            "message": "Backup uploaded successfully",
            "bucket": Config.S3_BUCKET,
            "file": backup_name
        })

    except ClientError as e:
        return jsonify({
            "error": str(e)
        }), 500