"""Generate the shared-password hash + a session secret for the phase-3 login gate.

    python -m scripts.gen_password_hash

Prompts (no echo) for the access password and prints the three .env lines to paste into
the service-dir .env (chmod 600, NEVER committed). The password is never stored or printed.
See DEPLOY_PLAN.md §3 and deploy/README.md.
"""
from __future__ import annotations

import getpass
import secrets
import sys

from server.auth import hash_password


def main() -> int:
    pw = getpass.getpass("Shared access password: ")
    pw2 = getpass.getpass("Confirm password:       ")
    if pw != pw2:
        print("ERROR: passwords do not match.", file=sys.stderr)
        return 1
    if len(pw) < 8:
        print("ERROR: password < 8 chars — too weak for the sole security boundary.", file=sys.stderr)
        return 1
    if len(pw) < 16:
        print("WARNING: password < 16 chars. Over plain HTTP on the LAN it is sniffable and is "
              "the ENTIRE security boundary; prefer a long random shared phrase.\n", file=sys.stderr)
    print("\n# --- paste into ~/sdtm-rag-service/.env  (chmod 600, NOT in git) ---")
    print("SDTM_RAG_AUTH_ENABLED=true")
    print(f"SDTM_RAG_SHARED_PASSWORD_HASH={hash_password(pw)}")
    print(f"SDTM_RAG_SESSION_SECRET={secrets.token_hex(32)}")
    print("# -------------------------------------------------------------------")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
