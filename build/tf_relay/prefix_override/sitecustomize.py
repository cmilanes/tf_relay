import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/cmilanes/tf_remapping/tf_relay/install/tf_relay'
