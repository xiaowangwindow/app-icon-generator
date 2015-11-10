#iOS开发所需的所有图片素材
#app icon screenshots generator

##中文
在iOS开发中，需要一整各种尺寸的icon，上传AppStore的时候，也需要一些列的屏幕截图。对于独立开发者来说，制作这些图片素材，虽然不是难事，但是需要耗费一定的时间。刚开始，我是使用sketch一张张手动生成的，一多了之后就有点烦，所以写了几个脚本自动生成。

###Xcode工程里用到的icon素材
使用 ` python icon_resize.py original_img.jpg ` 可以生成Xcode所需要的全套icon

###AppStore中的icon
在AppStore里面，要求一个 * 1024\*1024 * 的图片，而且是无透明通道的，所以jpg的就可以了, `python icon_1024.png icon_file_name`就行

###AppStore中的屏幕截图
使用 ` python screen_image_resize.py img1 img2 img3 ` 可以生成所有屏幕截图


##English
###icons in xcode project

in xcode project, we need icon sizes with iphone and ipad in **.png** format, `icon_resize.py` will generate all sizes, if your original icon file name is `a.jpg`, just run `python icon_resize.py a.jpg`, then you can see all sizes of icon appear in current directory.

###icon in AppStore

in AppStore, we need a * 1024\*1024 * icon, just run `python icon_1024.py a.jpg`

###Screenshots in AppStore
in AppStore, we also need six sizes screenshots contains iphone and ipad, just run `python screen_image_resize.py img1.jpg img2.jpg img3.jpg img4.jpg`
