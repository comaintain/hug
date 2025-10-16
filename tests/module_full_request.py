import hug


@hug.post("/test", output=hug.output_format.json)
def post(body, response):
    print(body)
    return {"message": "ok"}
