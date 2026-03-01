import uuid

def create_meet_link():
    sala = uuid.uuid4().hex[:12]
    return f"https://jitsi.0000750.xyz/skillswap-{sala}"