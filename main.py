import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chatgpt.com/c/c928b5e4-14b5-4b4b-9e3d-a005a1a3fdb1")
    page.goto("https://chatgpt.com/")
    page.get_by_placeholder("Message ChatGPT").fill("hi there ")
    page.get_by_test_id("send-button").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)