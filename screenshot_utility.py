from pathlib import Path
from datetime import datetime

def take_screenshot(driver, name="screenshot"):

    project_root = Path(__file__).resolve().parent
    screenshot_dir = project_root / "screenshots"
    screenshot_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = screenshot_dir / f"{name}-{timestamp}.png"

    driver.save_screenshot(str(filepath))
    print(f"Screenshot saved: {filepath}")