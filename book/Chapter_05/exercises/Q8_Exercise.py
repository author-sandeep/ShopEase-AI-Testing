try:
    config = ConfigModel(timeout="FAST")
except ValidationError as ve:
    print(f"Validation fault: {ve.errors()[0]['msg']}")