from . import wizard
def pre_init_check(cr):
    """Pre-install sanity check.
    Reserved for environment validations (e.g., version gating) if Kaizen policy
    later requires them. Returns True to allow installation.
    """
    return True