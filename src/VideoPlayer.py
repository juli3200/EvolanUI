########################################################################
from PySide6.QtCore import QStandardPaths, Qt, Slot, QDir, QUrl, QSize
from PySide6.QtGui import QAction, QIcon, QKeySequence, QScreen
from PySide6.QtWidgets import QDialog, QFileDialog, QWidget, QVBoxLayout, QListWidgetItem
from PySide6.QtMultimedia import QMediaPlayer, QAudio, QAudioOutput, QMediaFormat
from PySide6.QtMultimediaWidgets import QVideoWidget

# IMPORT Custom widgets
from Custom_Widgets import *
# Import QAppSettings
from Custom_Widgets.QAppSettings import QAppSettings

########################################################################
# IMPORT Magic media detector
# INSTALLATION:
# Please read the installation instructions here
# https://github.com/ahupp/python-magic
import magic
########################################################################

import os
import sys

class VideoPlayer():
    def __init__(self, ui):
        super(VideoPlayer, self).__init__()
        self.main = ui.ui  # Store the main instance
        self.mainW = ui  # Store the main instance

        # INITIALIZE APP SETTINGS
        settings = QSettings()
        # CURRENT THEME NAME
        theme = settings.value("ICONS-COLOR")
        # icons folder
        self.iconsFolder = theme.replace("#", "")

        ########################################################################
        # CREATE MEDIA PLAYER
        ########################################################################
        self.player =  QMediaPlayer()

        self.playlist = []  # FIXME 6.3: Replace by QMediaPlaylist?
        self.playlist_index = -1
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.player.errorOccurred.connect(self.player_error)
        
        
        ########################################################################
        # CREATE VIDEO WIDGET
        ########################################################################
        self.videoWidget = QVideoWidget()
        # Add video widget to player
        self.player.setVideoOutput(self.videoWidget)

        # Create video container
        self.videoContainer = QWidget(self.main.videoPlayerWidget)
        self.lay = QVBoxLayout(self.videoContainer)
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.videoWidget)

        self.main.videoLayout.addWidget(self.videoContainer)

        ########################################################################
        # PLAY MEDIA
        ########################################################################
        self.player.play()

        ########################################################################
        # NAV BUTTONS
        ########################################################################
        self.main.openMediaBtn.clicked.connect(lambda: self.openFile())
        self.main.playBtn.clicked.connect(lambda: self.play())

        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        self.player.playbackStateChanged.connect(self.mediaStateChanged)

        self.main.mediaProgress.valueChanged.connect(self.setPosition)

        self.main.volumeSlider.valueChanged.connect(self.updateMediaVolume)
        self.main.volumeBtn.clicked.connect(lambda: self.muteMediaPlayer())
        self.updateMediaVolume(self.audio_output.volume())

        self.main.stopMediaBtn.clicked.connect(lambda: self.stopMediaPlayer())
        self.main.prevMediaBtn.clicked.connect(lambda: self.playlist.previous())
        self.main.nextMediaBtn.clicked.connect(lambda: self.playlist.next())

        self.main.videoFilesWidget.itemClicked.connect(self.checkListItem)

        self.mediaStateChanged(self.player.playbackState())

    ########################################################################
    # SELECT MEDIA FILE
    ########################################################################
    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self.mainW, "Open Media",
                                                  QDir.homePath())
        if fileName:
            self.appendToPlaylist(fileName)
            

    ########################################################################
    # APPEND MEDIA TO PLAYLIST
    ########################################################################
    def appendToPlaylist(self, fileName):
        fileType, x = magic.from_file(fileName, mime=True).split("/")

        if fileType == "video" or fileType == "audio":
            icon = QIcon()
            self.listItem = QListWidgetItem()
            self.listItem.setText(os.path.basename(fileName))
            self.listItem.setWhatsThis(fileName)

            if fileType == "video":
                icon.addFile(f"theme-icons:{self.iconsFolder}/feather/video.png", QSize(24, 24), QIcon.Normal, QIcon.Off)
                self.listItem.setIcon(icon)
                self.main.videoFilesWidget.addItem(self.listItem)

    ########################################################################
    # CHECK CLICKED LIST ITEM
    ########################################################################
    def checkListItem(self, item):
        url = item.whatsThis()
        self.player.stop()
        self.player.setSource(url)
        self.player.play()
                

    ########################################################################
    # PLAY OR PAUSE MEDIA
    ########################################################################
    def play(self):
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    ########################################################################
    # UPDATE PLAY ICON
    ########################################################################
    def mediaStateChanged(self, state):
        icon = QIcon()
        if self.player.playbackState() == QMediaPlayer.PlayingState:
            icon.addFile(f"theme-icons:{self.iconsFolder}/feather/pause-circle.png", QSize(), QIcon.Normal, QIcon.Off)
            self.main.playBtn.setIcon(icon)
        else:
            icon.addFile(f"theme-icons:{self.iconsFolder}/feather/play-circle.png", QSize(), QIcon.Normal, QIcon.Off)
            self.main.playBtn.setIcon(icon)

    ########################################################################
    # UPDATE MEDIA PROGRESS
    ########################################################################
    def positionChanged(self, position):
        self.main.mediaProgress.setValue(position)
        self.main.playedMediaDuration.setText(str(self.convertMillis(position)))


    ########################################################################
    # UPDATE MEDIA DURATION
    ########################################################################
    def durationChanged(self, duration):
        self.main.mediaProgress.setRange(0, duration)
        # print(self.player.duration())
        self.main.totalMediaDuration.setText(str(self.convertMillis(self.player.duration())))

    ########################################################################
    # SET PLAYER POSITION
    ########################################################################
    def setPosition(self, position):
        self.player.setPosition(position)

    ########################################################################
    # UPDATE MEDIA VOLUME
    ########################################################################
    def updateMediaVolume(self, value):
        self.audio_output.setVolume(value)
        icon = QIcon()
        if value > 50:
            icon.addFile(f"theme-icons:{self.iconsFolder}/feather/volume-2.png", QSize(), QIcon.Normal, QIcon.Off)
            self.main.volumeBtn.setIcon(icon)

        elif value < 51 and value > 10:
            icon.addFile(f"theme-icons:{self.iconsFolder}/feather/volume-1.png", QSize(), QIcon.Normal, QIcon.Off)
            self.main.volumeBtn.setIcon(icon)

        elif value < 11 and value > 0:
            icon.addFile(f"theme-icons:{self.iconsFolder}/feather/volume.png", QSize(), QIcon.Normal, QIcon.Off)
            self.main.volumeBtn.setIcon(icon)

        else:
            icon.addFile(f"theme-icons:{self.iconsFolder}/feather/volume-x.png", QSize(), QIcon.Normal, QIcon.Off)
            self.main.volumeBtn.setIcon(icon)

        if self.main.volumeSlider.value() != value:
            self.main.volumeSlider.setValue(value)

    ########################################################################
    # MUTE MEDIA VOLUME
    ########################################################################
    def muteMediaPlayer(self):
        icon = QIcon()
        if self.audio_output.isMuted():
            self.audio_output.setMuted(False)
            self.updateMediaVolume(self.audio_output.volume())
        else:
            self.audio_output.setMuted(True)
            icon.addFile(f"theme-icons:{self.iconsFolder}/feather/volume-x.png", QSize(), QIcon.Normal, QIcon.Off)
            self.main.volumeBtn.setIcon(icon)

    ########################################################################
    # STOP MEDIA
    ########################################################################
    def stopMediaPlayer(self):
        self.player.stop() 
        self.main.mediaProgress.setValue(0)

    ########################################################################
    # GENERATE MEDIA TIME
    ########################################################################
    def convertMillis(self, millis):
        millis = int(millis)
        seconds=(millis/1000)%60
        seconds = int(seconds)
        minutes=(millis/(1000*60))%60
        minutes = int(minutes)
        hours=(millis/(1000*60*60))%24

        return "%d:%d:%d" % (hours, minutes, seconds)

    @Slot(QMediaPlayer.Error, str)
    def player_error(self, error, error_string):
        print(error_string, file=sys.stderr)

