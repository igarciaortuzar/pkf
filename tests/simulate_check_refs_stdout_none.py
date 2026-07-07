import runpy
import sys

class FakeOut:
    encoding = None
    def write(self, s): pass
    def flush(self): pass
    def writelines(self, lines): pass

orig_stdout = sys.stdout
try:
    sys.stdout = FakeOut()
    try:
        runpy.run_path("tools/check_refs.py", run_name="__main__")
    except SystemExit as e:
        code = e.code
        sys.stderr.write(f"EXIT_CODE:{code}\n")
    except Exception:
        import traceback
        traceback.print_exc(file=sys.stderr)
finally:
    sys.stdout = orig_stdout
