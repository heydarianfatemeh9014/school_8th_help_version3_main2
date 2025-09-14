[app]

# Basic app info
title = My Application
package.name = school_grades_help
package.domain = org.test
source.dir = codes
source.include_exts = py,png,jpg,jpeg
source.include_patterns = imagess/*

version = 0.1
requirements = python3,kivy

orientation = portrait
fullscreen = 0

# Android settings
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.build_tools_version = 33.0.2
android.ndk_path = ~/.buildozer/android/platform/android-ndk-r25b
android.ndk_version = 25.2.9519653
android.sdk_path = ~/.buildozer/android/platform/android-sdk
android.skip_update = True
android.allow_backup = True
android.add_assets = imagess

# Python for Android (p4a) settings
p4a.bootstrap = sdl2

# iOS settings (optional)
ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master
ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.10.0
ios.codesign.allowed = false

[buildozer]
log_level = 2
warn_on_root = 1
