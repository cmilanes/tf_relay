from typing import Iterable, Optional, Set


def normalize_frame_id(frame_id: str) -> str:
    return frame_id.lstrip('/')


def apply_frame_prefix(
    frame_id: str,
    frame_prefix: str,
    unprefixed_frames: Optional[Iterable[str]] = None,
) -> str:
    """Normalize and apply a frame prefix only when needed.

    Nav2 and tf2 expect frame ids without leading '/'.
    """
    normalized_frame_id = normalize_frame_id(frame_id)

    if not normalized_frame_id:
        return normalized_frame_id

    unprefixed: Set[str] = {
        normalize_frame_id(frame) for frame in (unprefixed_frames or [])
    }
    if normalized_frame_id in unprefixed:
        return normalized_frame_id

    if normalized_frame_id.startswith(frame_prefix):
        return normalized_frame_id

    return f'{frame_prefix}{normalized_frame_id}'
