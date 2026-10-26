import secrets, string, sys
def generate(length=16):
    if length < 8: raise ValueError("length must be at least 8")
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(alphabet) for _ in range(length))
if __name__ == "__main__":
    print(generate(int(sys.argv[1]) if len(sys.argv) > 1 else 16))
