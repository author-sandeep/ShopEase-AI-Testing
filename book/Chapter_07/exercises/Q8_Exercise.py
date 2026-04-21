def extract_status_defensively(payload: dict) -> str:
    metadata = payload.get("metadata", {})
    server = metadata.get("server", {})
    return server.get("status", "UNKNOWN")