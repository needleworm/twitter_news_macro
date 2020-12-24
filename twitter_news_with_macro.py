"""
Author : Byunghyun Ban
Last Modification : 2020.12.24.
bhban@kakao.com
https://github.com/needleworm/twitter_news_macro
"""

from selenium import webdriver
import pywinmacro as pw
import pyperclip as pc
import time


class NewsBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.search_url = "https://google.com/search?tbm=nws&q="
        self.news_text = ""
        self.splt = []

    def kill(self):
        self.driver.quit()

    def refresh(self):
        pw.key_press_once("f5")

    def scrap_news(self, id, ps, keyword):
        self.driver.get(self.search_url + keyword)
        time.sleep(5)

        # 클릭할 좌표를 지정합니다
        location = (226, -607)

        # 화면을 클릭합니다.
        pw.click(location)

        # Ctrl + A를 누릅니다.
        pw.ctrl_a()
        time.sleep(1)

        # Ctrl + C를 누릅니다.
        pw.ctrl_c()
        # Ctrl + C를 누릅니다.
        pw.ctrl_c()
        # Ctrl + C를 누릅니다.
        pw.ctrl_c()
        # Ctrl + C를 누릅니다.
        pw.ctrl_c()
        time.sleep(3)

        # 클립보드의 내용물을 뽑아옵니다.
        self.news_text = pc.paste()

        # 뉴스 텍스트를 스플릿합니다.
        self.splt = self.news_text.split("\r\n\r\n")[2:-1]

        # 트위터에 접속합니다.
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        # 아이디를 입력합니다.
        pw.typing(id)
        # 탭 키를 칩니다.
        pw.key_press_once("tab")
        # 비밀번호를 입력합니다.
        pw.typing(ps)
        # 엔터키를 칩니다.
        pw.key_press_once("enter")
        time.sleep(5)

        for el in self.splt:
            # 트위터에 글을 올립니다.
            # 게시물 작성 페이지로 이동
            self.driver.get("https://twitter.com/intent/tweet")
            time.sleep(2)
            # 내용물 입력
            pw.type_in(el)
            time.sleep(1)

            # Ctlr + Enter 누르기
            pw.key_on("control")
            pw.key_on("enter")
            pw.key_off("control")
            pw.key_off("enter")

            time.sleep(10)
