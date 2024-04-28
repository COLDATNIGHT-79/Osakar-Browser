from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import *
from urllib.parse import urlparse
import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

       
        self.history = []
        self.bookmarks = []

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        next_btn = QAction('Forward', self)
        next_btn.triggered.connect(self.browser.forward)
        navtb.addAction(next_btn)

        reload_btn = QAction('Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

       
        self.url_bar = QLineEdit()
        self.url_bar.setFixedHeight(30)  
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.url_bar)

        
        self.browser.urlChanged.connect(self.update_url)

   
        bookmark_btn = QAction('Bookmark', self)
        bookmark_btn.triggered.connect(self.bookmark_page)
        navtb.addAction(bookmark_btn)
        self.browser.urlChanged.connect(self.track_history)

    def navigate_home(self):
     self.browser.setUrl(QUrl.fromLocalFile('E:/vpn/homepage.html'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        parsed_url = urlparse(url)
        if bool(parsed_url.netloc) and bool(parsed_url.scheme):
            self.browser.setUrl(QUrl(url))
        else:
            search_url = 'https://www.google.com/search?q=' + url
            self.browser.setUrl(QUrl(search_url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def track_history(self, url):
        self.history.append(url)

    def bookmark_page(self):
        self.bookmarks.append(self.browser.url())

app = QApplication(sys.argv)
app.setStyleSheet("""
    QWidget {
        background-color: #2b2b2b;
        color: #bdbdbd;
        border: 1px solid #3a3a3a;
    }
    QLineEdit {
        background-color: #3a3a3a;
        color: #bdbdbd;
    }
    QToolBar {
        background-color: #3a3a3a;
        border: 1px solid #3a3a3a;
    }
    QPushButton {
        background-color: #3a3a3a;
        color: #bdbdbd;
    }
""")
app.setApplicationName('Cold,s Epic Web Browser')
window = MainWindow()
app.exec_()