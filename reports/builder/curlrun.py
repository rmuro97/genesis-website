# Run a builder script with urllib.request.urlopen routed through curl (Nasdaq's CDN blocks Python's urllib but not curl).
import io, runpy, subprocess, sys, urllib.request
def _open(req, timeout=30, *a, **k):
    url = req.full_url if isinstance(req, urllib.request.Request) else req
    hdrs = dict(req.header_items()) if isinstance(req, urllib.request.Request) else {}
    cmd = ["curl", "-sS", "--fail", "--compressed", "--max-time", str(int(timeout or 30))]
    for kk, v in hdrs.items():
        if kk.lower() != "accept-encoding":
            cmd += ["-H", f"{kk}: {v}"]
    out = subprocess.run(cmd + [url], capture_output=True)
    if out.returncode:
        raise urllib.error.URLError(out.stderr.decode()[:200])
    return io.BytesIO(out.stdout)
urllib.request.urlopen = _open
script = sys.argv[1]; sys.argv = sys.argv[1:]
runpy.run_path(script, run_name="__main__")
