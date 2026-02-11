from tf_relay.frame_utils import apply_frame_prefix


def test_apply_frame_prefix_adds_prefix():
    assert apply_frame_prefix('base_link', 'robot_0/') == 'robot_0/base_link'


def test_apply_frame_prefix_strips_leading_slash():
    assert apply_frame_prefix('/odom', 'robot_0/') == 'robot_0/odom'


def test_apply_frame_prefix_does_not_double_prefix():
    assert apply_frame_prefix('robot_0/base_scan', 'robot_0/') == 'robot_0/base_scan'


def test_apply_frame_prefix_handles_empty_frame():
    assert apply_frame_prefix('', 'robot_0/') == ''


def test_apply_frame_prefix_keeps_shared_map_frame_unprefixed():
    assert apply_frame_prefix('map', 'robot_0/', ['map']) == 'map'


def test_apply_frame_prefix_keeps_shared_map_frame_unprefixed_when_absolute():
    assert apply_frame_prefix('/map', 'robot_0/', ['map']) == 'map'
