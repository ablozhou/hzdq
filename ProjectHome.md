## 功能特点 ##

---

支持Unihan最新版本5.2的所有74394个汉字查询。
大多具有拼音，部分具有朝鲜谚文，朝鲜罗马字，日语音读，日语训读，或越南音标。
部分支持五笔，仓颉，四角号码，郑码，偏旁，笔画数，笔顺查询。
部分具有英语解释。

Unicode 里汉字字块包括汉日朝统一表意字（ CJK 、汉统， 20940 个（GBK收录其中20902个）；汉日朝统一表意字扩充甲（ Ext-A 、扩甲， 6582 个）（以上为汉字GB18030-2000收录，微软windows 和普通输入法、字库一般只支持到此标准）；汉日朝统一表意字扩充乙（ Ext-B 、扩乙， 42711 个），（以上为GB18030-2005收录）；汉日朝统一表意字扩充丙（ Ext-C 、扩丙， 4149 个）、汉日朝部首增补、汉日朝笔 划、汉日朝兼容表意字、汉日朝兼容表意字增补等。

详见好南儿上海话写的文章：http://shanghaian.72pines.com/how-to-input-difficult-han-characters-in-windows/#comment-78
我的翻译：
http://abloz.com/2010/02/16/translation-windows-secluded-ancient-chinese-character-input-method.html

已知问题：
windows下字符输入和显示范围比《汉字大全》小很多。

基于python 2.6+

基于wxpython 2.8+

基于ubuntu 9.10，windows XP中文版

基于unicode 5.2 2009.9最新版本

推荐在ubuntu 上使用本字典。



---

The HZDQ(hanzidaquan) dictionary you can consult all Chinese, Japanese, Korean, Vietnamese Han ideographs. It base on recent Unicode Han database 5.2. Most of them has a Hanyupinyin or JapaneseKun, JapaneseOn, Korean Hangul, Korean Roman, Vietnamese pronunciation and an English gloss.  It contains of 71424 Han ideographs.

Needs:

python 2.6+

wxpython 2.8+

ubuntu 9.10 with Chinese language support.
windows XP Chinese version.


## 示例： ##

---

巭(上“功”下“夫”）

Unicode:0x5ded
朝鲜罗马字:pwu
五笔:alfw
郑码:bibo
笔画数:9
部首:工
笔顺:121531134


烎（上“开”下“火”）

Unicode:0x70ce
汉语拼音:yín
五笔:ffou
郑码:aeuo
笔画数:8
部首:火
笔顺:11324334


𨃴（左“足”右“骨”）

Unicode:0x280f4
越南语读音:gót

䶐（左“鼻”右“會”）

Unicode:0x4d90
汉语拼音:wài/huì
粤语读音:fai3
英语解释:    to take breath; snoring; snorting

䲥（上“九”下“鳥”）

Unicode:0x4ca5
粤语读音:gau1
英语解释:    (same as 鳩) the pigeon; the turtle dove

后面三个字在一般的字典中查不到的哦。
可以试一下金山词霸的在线版 http://hanyu.iciba.com

本字典比普通字典多字。

## 用法说明 ##

---


windows环境：

1.下载python2.6+

http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi

2.下载wxpython2.8+

http://downloads.sourceforge.net/wxpython/wxPython2.8-win32-unicode-2.8.10.1-py26.exe

3.执行hzdq.pyw

在输入框中输入或粘贴汉字，点搜索(search)


---

Linux 环境：

1.安装python2.6+

2.安装wxpython 2.8+

3.执行hzdq.pyw

在输入框中输入或粘贴汉字，点搜索(search)



---

周海汉(ablo zhou)

2010.2.6