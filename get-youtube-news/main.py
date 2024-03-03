from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

with open("channels.txt") as file:
    channels = file.readlines()

driver.get(f"https://www.youtube.com/{channels[0]}/videos")
consent_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Accept all']")
consent_button.click()

data = {}
with open("videos.txt", "w") as file:
    file.write("")
for channel in channels:
    channel = channel.strip("\n")
    print(channel)
    driver.get(f"https://www.youtube.com/{channel}/videos")

    videos = driver.find_elements(By.CSS_SELECTOR, "a[id=video-title-link]")
    videos = videos[:3]
    with open("videos.txt", "a") as file:
        file.write(f"\n\n{channel}\n--------------------------------------------\n")
    for video in videos:
        link = video.get_attribute("href")
        split_link = link.split(".")
        ss_youtube = "ss" + split_link[1]
        ss_link = f"{split_link[0]}.{ss_youtube}.{split_link[2]}"

        content = [
            f"title: {str(video.text.encode("utf-8")).split("'")[1]}\n",
            f"video-link: {str(link.encode("utf-8")).split("'")[1]}\n",
            f"download-link: {str(ss_link.encode("utf-8")).split("'")[1]}\n",
            "--------------------------------------------\n"
        ]
        with open("videos.txt", "a") as file:
            file.writelines(content)
