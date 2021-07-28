def successful(data: dict = None):
    return {"data": data, "status": "success"}


def error(data: dict = None):
    return {"data": data, "status": "failed"}
