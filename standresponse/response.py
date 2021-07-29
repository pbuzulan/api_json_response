def successful(data: dict = None):
    return {"data": data, "status": "success"}


def error(data: dict = None):
    return {"data": data, "status": "failed"}


def pagination(items: list, total_items: int, page_index: int, page_size: int):
    total_pages = 0
    if page_size != 0:
        total_pages = total_items // page_size
        if total_items != total_pages * page_size:
            total_pages += 1
    data = {"items": items, "total_items": total_items, "page_index": page_index, "page_size": page_size,
            "total_pages": total_pages}
    return {"data": data, "status": "success"}
