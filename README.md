#app icon screenshots generator

###icons in xcode project

in xcode project, we need icon sizes with iphone and ipad in **.png** format, `icon_resize.py` will generate all sizes, if your original icon file name is `a.jpg`, just run `python icon_resize.py a.jpg`, then you can see all sizes of icon appear in current directory.

###icon in AppStore

in AppStore, we need a * 1024\*1024 * icon, just run `python icon_1024.py a.jpg`

###Screenshots in AppStore
in AppStore, we also need six sizes screenshots contains iphone and ipad, just run `python screen_image_resize.py img1.jpg img2.jpg img3.jpg img4.jpg`
