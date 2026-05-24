import re
from pathlib import Path
from urllib.parse import quote


OBSIDIAN_IMAGE_RE = re.compile(r"!\[\[([^\]|]+)(?:\|[^\]]+)?\]\]")


def on_page_markdown(markdown, page, config, files):
    def replace_image(match):
        image_name = match.group(1).strip()
        image_path = Path("assets") / image_name
        quoted_path = quote(image_path.as_posix())
        return f"![{image_name}]({quoted_path})"

    return OBSIDIAN_IMAGE_RE.sub(replace_image, markdown)
